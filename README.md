# Ceneo Scraper

Ceneo Scraper is a Python web application for downloading and analying reviews from [Ceneo](https://ceneo.pl)

## Prerequisites

Create virtual environment:

```bash
python -m venv .venv
```

Source the environment (bash):

```bash
source .venv/bin/activate
```

Source the environment (Powershell):

```powershell
.venv/bin/Activate.ps1
```

> Note: If the above command doesn't work on Powershell you have to allow scripts to be run. You can achieve this with:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Starting the server

```python
flask --app flaskr run --debug
```

By default application binds to [localhost:5000](http://localhost:5000).

## Usage

See "How to use this?" section in [ABOUT.md](ABOUT.md)

## Contributing

Pull requests are welcome, however I do not guarantee fast response.

## Credits

- [Lorc](https://lorcblog.blogspot.com/) for providing [Favicon](flaskr/static/images/favicon.svg) icon via [Game-Icons.net](https://game-icons.net/1x1/lorc/magnifying-glass.html)

## License

This repository is licensed under [MIT](LICENSE).
