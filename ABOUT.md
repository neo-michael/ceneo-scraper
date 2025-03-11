# About

## What it does?

This web app downloads and parses reviews from [Ceneo.pl](https://ceneo.pl).

## How does it do it?

Product page is fetched asynchronously via [httpx](https://www.python-httpx.org/), which is then parsed by [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). Information is mostly queried by tags and class attributes and it's done in error-prone manner.

## How to use it?

> Note: Make sure the web server is running. Check out [README.md](README.md) to figure out how to do this.

1. Find your product of interest on [Ceneo.pl](https://ceneo.pl).
2. Note down the product id:
    > You can find it in the url, right after the [TLD](https://en.wikipedia.org/wiki/Top-level_domain) e.g.:
    > For this product: "https://www.ceneo.pl/138536500" the id is 138536500

3. Open [localhost:5000](http://localhost:5000) in your browser.
4. Select "Extract reviews".
5. Enter the product id from step 2.
6. Click extract.
7. Wait for the page to refresh.
    > Also admire the loading animation :)
8. Done! You can now browse reviews of your product.