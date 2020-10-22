# Home Assistant - Nimrod-messenger.io integration
[Nimrod-Messenger](https://https://www.nimrod-messenger.io/) integration [Home Assistant](https://www.home-assistant.io/)

=========================
## Table of contents:
- [How to get api-key](#how-to-get-api-key)
- [Home Assistant usage](#home-assinstant-usage)

------------
## How to get api-key
You must obtain an API key before using this notify component. The easiest way: Let's conversating with [Nimrod-messenger](https://m.me/251459615313202) here. The easy way: follow this [instruction](https://www.nimrod-messenger.io/).

## Home Assistant usage:
```yaml
notify:
  - name: "Nimrod-messenger"
    platform: nimrod
    api_key: "your-api-key"
