import httpx
import json

from bs4 import BeautifulSoup
from flask import current_app

from .review_parser import ReviewParser


async def save_reviews_to_json(product_id):
    reviews = await _fetch_reviews(product_id)

    with open(f"./reviews/{product_id}.json", "w") as fp:
        fp.write("[")
        fp.write(",".join((rev.to_json_str() for rev in reviews)))
        fp.write("]")


async def _fetch_reviews(product_id):
    base_url = "https://www.ceneo.pl"
    location = f"/{product_id}#tab=reviews"

    reviews = []

    async with httpx.AsyncClient(
        headers=current_app.config["HEADERS"], http2=True, follow_redirects=True,
    ) as client:

        page = 1

        # Ceneo only shows maximum of 50 pages
        while page <= 50:
            print(f"Fetching page {page}")
            response = await client.get(base_url + location)
            (new_reviews, next_location) = parse_reviews(response.text)

            reviews += new_reviews
            if not next_location:
                break

            location = next_location
            page += 1

    return reviews


def parse_reviews(contents):
    reviews = []

    document = BeautifulSoup(contents, "lxml")

    # Contains all reviews on the page
    review_div = document.find(
        "div", class_="js_product-reviews js_reviews-hook js_product-reviews-container"
    )

    if not review_div:
        return (reviews, "")

    reviews_tag = review_div.find_all(
        "div", class_="user-post user-post__card js_product-review"
    )

    review_parser = ReviewParser()
    for review in reviews_tag:
        reviews.append(review_parser.parse(review))

    next_location = document.find(
        "a", class_="pagination__item pagination__next", href=True
    )

    if not next_location:
        return (reviews, "")

    return (reviews, next_location["href"])
