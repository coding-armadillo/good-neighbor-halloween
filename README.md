<div align="center">
    <img src="https://cdn2.iconfinder.com/data/icons/free-color-halloween-icons/24/Pumpkin-Lamp_01-512.png" alt="logo" height="196">
</div>

# good-neighbor-halloween

## Getting Started

### Install

```zsh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Use `pip install -r requirements-dev.txt` for development. It will install `pylint` and `black` to enable linting and auto-formatting.

### Setup

Create a `.env` file to configure the AWS S3 bucket

```zsh
touch .env
```

And put down the the following information

```
GCP_KEY=...
MAPQUEST_KEY=...
MAP_LAT=...
MAP_LNG=...
```

## Credits

- [Logo][1] by [Alpár-Etele Méder][2]
- [Halloween Freebie icon set][3] by [roundicons.com][4]

[1]: https://www.iconfinder.com/icons/1531889/halloween_lamp_pumpkin_icon
[2]: https://www.iconfinder.com/pocike
[3]: https://www.iconfinder.com/iconsets/halloween-freebie
[4]: https://www.iconfinder.com/roundicons
