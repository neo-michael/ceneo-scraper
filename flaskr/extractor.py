import httpx
from bs4 import BeautifulSoup

async def save_reviews_to_json(product_id):
    reviews = await _fetch_reviews(product_id)

    for review in reviews:
        pass


async def _fetch_reviews(product_id):
    base_url = "https://www.ceneo.pl/"
    location = f"{product_id}#tab=reviews"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0, i",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    }

    async with httpx.AsyncClient(headers=headers, http2=True, follow_redirects=True) as client:
        while True:
            response = await client.get(base_url + location)
            document = BeautifulSoup(response.text, 'lxml')

            
            
            next_button_query = document.find_all('a', class_="pagination__item pagination__next")

            if len(next_button_query) == 0:
                break
            
            location = next_button_query["href"]



