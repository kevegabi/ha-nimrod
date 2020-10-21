"""Nimrod-messenger platform for notify component."""
import json
import logging

from aiohttp.hdrs import CONTENT_TYPE
import requests
import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TARGET,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONTENT_TYPE_JSON, HTTP_OK
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_API_KEY = "api-key"
BASE_URL = "https://www.nimrod-messenger.io/api/v1/message"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {vol.Required(CONF_API_KEY): cv.string}
)


def get_service(hass, config, discovery_info=None):
    """Get the Nimrod notification service."""
    return NimrodNotificationService(config[CONF_API_KEY])


class NimrodNotificationService(BaseNotificationService):
    """Implementation of a notification service for the Nimrod-messenger service."""

    def __init__(self, api_key):
        """Initialize the service."""
        self.page_api_key = api_key

    def send_message(self, message="", **kwargs):
        """Send some message."""
        payload = {"spi-key": self.page_api_key}
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA)

        body_message = {"text": message}

        if data is not None:
            body_message.update(data)
            # Only one of text or attachment can be specified
            if "attachment" in body_message:
                body_message.pop("text")

        if not targets:
            _LOGGER.error("At least 1 target is required")
            return

            body = {
                "message": body_message,
            }
            resp = requests.post(
                BASE_URL,
                data=json.dumps(body),
                params=payload,
                headers={CONTENT_TYPE: CONTENT_TYPE_JSON},
                timeout=10,
            )
            if resp.status_code != HTTP_OK:
                log_error(resp)


def log_error(response):
    """Log error message."""
    obj = response.json()
    error_message = obj["error"]["message"]
    error_code = obj["error"]["code"]

    _LOGGER.error(
        "Error %s : %s (Code %s)", response.status_code, error_message, error_code
    )