"""Nimrod-messenger platform for notify component."""
from http import HTTPStatus
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
from homeassistant.const import CONTENT_TYPE_JSON
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_API_KEY = "api_key"
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

        headers = {'Content-type': 'application/json' }

        nimrod_message = {'message': message, 'api_key': self.page_api_key}

        resp = requests.post(BASE_URL, data=json.dumps(nimrod_message), headers=headers)

        if resp.status_code != HTTPStatus.OK:
            log_error(resp)


def log_error(response):
    """Log error message."""
    obj = response.json()
    error_message = obj["error"]["message"]
    error_code = obj["error"]["code"]

    _LOGGER.error(
        "Error %s : %s (Code %s)", response.status_code, error_message, error_code
    )