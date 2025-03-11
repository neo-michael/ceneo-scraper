import httpx
from bs4 import BeautifulSoup

from .review_parser import ReviewParser


async def save_reviews_to_json(product_id):
    reviews = await _fetch_reviews(product_id)

    for review in reviews:
        pass


async def _fetch_reviews(product_id):
    base_url = "https://www.ceneo.pl"
    location = f"/{product_id}#tab=reviews"

    # headers copy pasted from browser
    headers = {
        "Host": "www.ceneo.pl",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Cookie": "__utmf=7fa4b5375869df026ecc0dbc6666649b_k2wCRI6tAVSgxOOwMsWh%2Bvo35Yf981ST; __RequestVerificationToken=exT5ivLDvNUJF5e9iOpNgB9Lb1ztE1guvdU8eAXHM4F9QBhjywd6hnBK9wo9HH-arY3--lxxStKVDR8DiZK-2II0HG27tkIrgi_Bp2dyu-k1; sv3=1.0_49627aeb-fe7d-11ef-bcd5-744055f64b69; userCeneo=ID=b72bccd5-ccc5-4bb7-9b3a-29a8bc53a463; ai_user=TSAGU|2025-03-11T13:32:34.271Z; ai_session=N5uNG|1741699954374|1741699954374; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.49627aeb-fe7d-11ef-bcd5-744055f64b69; ga4_ga_K2N2M0CBQ6=GS1.2.1741699954.1.1.1741699960.0.0.2090569; _gcl_au=1.1.1060162402.1741699960; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUU9HdUlBUU9HdUlBR3lBQkJQTEJnRXNBUF9nQUFBQUFCNVlJTnBEN0JiQkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUJRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJSU5nQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRUd3a0FHQUFJSU5ob0FNQUFRUWJFUUFZQUFnZzJLZ0F3QUJCQnNaQUJnQUNDRFk2QURBQUVFR3lFQUdBQUlJTmtvQU1BQVFRYktRQVlBQWdnMldnQXdBQkJCc0EiLCJWZXJzaW9uIjoidjMifQ==; FPID=FPID2.2.pGbexB6zFAXcdxLfm3p7SZZDIKMmqoh6zB%2F77uMO2jc%3D; FPLC=GFU%2FdzQYQyb40SIYRrQSJx2h9rNbX%2BLfrKKKDBqaI%2B9HmsWxhLMZTnGnyhMkkt%2B12edHf4rgMIGuVdrvN5dEQhuspVMI1pH4kCyzJJTAz%2FxowVk%3D",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Priority": "u=0, i",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    }

    reviews = []

    async with httpx.AsyncClient(
        headers=headers, http2=False, follow_redirects=True,
    ) as client:
        i = 1
        while True:
            print(f"Fetching page {i}")
            response = await client.get(base_url + location)
            (new_reviews, next_location) = parse_reviews(response.text)

            reviews += new_reviews
            if not next_location:
                break

            location = next_location
            i += 1
    


def parse_reviews(contents):
    reviews = []

    document = BeautifulSoup(contents, "lxml")

    review_div = document.find(
        "div", class_="js_product-reviews js_reviews-hook js_product-reviews-container"
    )

    if not review_div:
        return (reviews, "")

    child_divs = review_div.find_all(
        "div", class_="user-post user-post__card js_product-review"
    )

    for child_div in child_divs:
        review_parser = ReviewParser()

        reviews.append(review_parser.parse(child_div))

    next_location = document.find(
        "a", class_="pagination__item pagination__next", href=True
    )

    if not next_location:
        return (reviews, "")

    return (reviews, next_location["href"])
