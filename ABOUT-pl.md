# Opis

## Do czego to służy?

Ta aplikacja webowa pobiera i przetwarza opinie z [Ceneo.pl](https://ceneo.pl).

Serwer przechowuje do 500 opinii dla danego produktu oraz pomaga w podjęciu decyzji kupna poprzez dane przedstawione na wykresie.

## Jak to działa?

Opinie o produkcie są pobierane asynchronicznie poprzez [httpx](https://www.python-httpx.org/), które są przetwarzane przez [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). Następnie dane są wyszukiwane poprzez tagi oraz atrybuty, ze zwróconą uwagą na błędy.

## Jak tego użyć?

> Notka: Upewnij się, że serwer jest włączony. Kroki potrzebne do uruchomienia serwera znajdują się w [README.md](README.md).

1. Wybierz produkt z [Ceneo.pl](https://ceneo.pl).
2. Zanotuj id tego produktu:
> Możesz znaleźć to id w pasku adresu, zaraz po ".pl/" np.:
> Dla tego produktu: "https://www.ceneo.pl/138536500" id to 138536500
3. Wejdź na [localhost:5000](http://localhost:5000).
4. Wybierz "Ekstraktuj opinie".
5. Wpisz id produktu z kroku 2.
6. Kilknij "Ekstraktuj"
7. Poczekaj aż strona się odświerzy.
> Między czasie możesz podziwiać animację ładowania :)
8. Gotowe! Teraz możesz przeglądać opinie o tym produkcie.