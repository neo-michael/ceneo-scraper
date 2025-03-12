# Ceneo Scraper

Ceneo Scraper to aplikacja webowa napisana w Pythonie do pobierania i analizowania opinii z [Ceneo](https://ceneo.pl)

## Zanim zaczniesz...

Utwórz wirtualne środowisko:

```
python -m venv .venv
```

Aktywuj środowisko (bash)

```
source .venv/bin/activate
```

Aktywuj środowisko (Powershell):

```
.venv/bin/Activate.ps1
```

> Notka: Jeżeli komenda powyżej zwróci błąd w powłoce Powershell, musisz ustawić poziom wykonywania skryptów. O tak:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Instalowanie

Używają menadżera pakietów [pip](https://pip.pypa.io/en/stable/) zainstaluj potrzebne biblioteki.

```
pip install -r requirements.txt
```

## Włączanie serwera

```
flask --app flaskr run --debug
```

Domyślnie aplikacja znajduję się pod tym adresem: [localhost:5000](http://localhost:5000).

## Użytkowanie

Zobacz sekcje "Jak tego użyć?" w [ABOUT-pl.md](ABOUT-pl.md)


## Wiki

Zobacz [WIKI-pl.md](WIKI-pl.md)


## Wkład i współpraca

"Pull request" są mile widziane, natomiast nie gwarantuje szybkiej odpowiedzi na nie.

## Podziękowania i uznania

- [Lorc](https://lorcblog.blogspot.com/) za ikonę [Favicon](flaskr/static/images/favicon.svg) ze strony [Game-Icons.net](https://game-icons.net/1x1/lorc/magnifying-glass.html)

## Licencja

To repozyterium posiada licencję [MIT](LICENSE).
