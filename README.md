# Home Assistant - Nimrod-messenger.io integration
[Nimrod-Messenger](https://https://www.nimrod-messenger.io/) integration [Home Assistant](https://www.home-assistant.io/)

=========================
## Table of contents:
- [How to get api-key](#how-to-get-api-key)
- [Home Assistant configuration](#home-assinstant-configuration)
- [Home Assistant usage example](#home-assistant-usage-example)

------------
## How to get api-key
You must obtain an API key before using this notify component. The easiest way: Let's conversating with [Nimrod-messenger](https://m.me/251459615313202) here. The easy way: follow this [instruction](https://www.nimrod-messenger.io/).

## Home Assistant configuration:
```yaml
notify:
  - name: "Nimrod-messenger"
    platform: nimrod
    api_key: "your-api-key"
```

## Home Assistant usage example:
Simple example, for sun down / shine notification.
```yaml
action:
  service: notify.nimrod-messanger
  data:
    message: "The sun is {% if is_state('sun.sun', 'above_horizon') %}up{% else %}down{% endif %}!"
```
