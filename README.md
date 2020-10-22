# Home Assistant - Nimrod-messenger.io integration
[Nimrod-Messenger](https://https://www.nimrod-messenger.io/) integration [Home Assistant](https://www.home-assistant.io/)

------------

## Table of contents:
- [How to install](#how-to-install)
- [How to get API key](#how-to-get-api-key)
- [Home Assistant configuration](#home-assinstant-configuration)
- [Home Assistant usage example](#home-assistant-usage-example)
- [Copyright](#copyright)

------------

## How to install
Easiest way, is [HACS](https://hacs.xyz/)!
- Install [HACS installer](https://hacs.xyz/docs/installation/manual) on your Home Assistant.
- Click to the Integration menu
- Click the three point in the upper right corder, and select Custom Repositories
- Insert this [link](https://github.com/kevegabi/ha-nimrod/) to the 'Add custom repository URL', and select 'Integration' from the Category popup
- Click to Add button
- Click to the '+' sign in the bottm right corner, and find the Nimrod-messenger component. Click to the 'Install this repository in HACS'
- Enjoy

Hardest way:
- Create a folder nammed 'ha-nimrod' under the custom_components. 
- Copy all the files (__init__.py, manifest.json, notify.py) the 'ha-nimrod'.

## How to get API key
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
  service: notify.nimrod_messenger
  data:
    message: "The sun is {% if is_state('sun.sun', 'above_horizon') %}up{% else %}down{% endif %}!"
```
## Copyright
- Nimrod-messanger copyright © xureiLab
- Nimrod-messenger HA integration copyright © kevegabi
