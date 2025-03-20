import httpx
import json

from bs4 import BeautifulSoup
from flask import current_app, url_for

from .review_parser import ReviewParser

from ..models.product import Product
from ..scripts.utils import convert_to_csv, convert_to_xlsx

# TODO: rename to save_review_to_file
async def save_reviews_to_json(product_id):
    reviews, product = await _fetch_reviews(product_id)
    
    product.id = product_id

    for review in reviews:
        product.pros_count += len(review.pros)
        product.cons_count += len(review.cons)

    product.json = url_for("product.download", product_id=product_id, ext="json")
    product.csv = url_for("product.download", product_id=product_id, ext="csv")
    product.xlsx = url_for("product.download", product_id=product_id, ext="xlsx")

    with open(f"./products/{product_id}.json", 'w') as fp2:
        fp2.write(product.to_json_str())
    
    with open(f"./reviews/{product_id}.json", "w") as fp:
        fp.write("[")
        fp.write(",".join((rev.to_json_str() for rev in reviews)))
        fp.write("]")
    
    convert_to_csv(reviews, f"./reviews/{product_id}.csv")
    convert_to_xlsx(f"./reviews/{product_id}.csv", f"./reviews/{product_id}.xlsx")

async def _fetch_reviews(product_id):
    base_url = "https://www.ceneo.pl"
    location = f"/{product_id}#tab=reviews"
    max_pages = 50

    reviews = []
    product = None
    is_first_page = True
    page = 1

    async with httpx.AsyncClient(**current_app.config["HTTP_CONFIG"]) as client:
        while page <= max_pages:
            print(f"Fetching page {page}")
            response = await client.get(base_url + location)
            new_reviews, next_location, product_info = parse_reviews(response.text, is_first_page)

            reviews.extend(new_reviews)

            if is_first_page:
                product = product_info
                is_first_page = False

            if not next_location:
                break

            location = next_location
            page += 1

    return (reviews, product)


def parse_reviews(contents, is_first_page):
    reviews = []
    product = None

    document = BeautifulSoup(contents, "lxml")

    if is_first_page:
        product = _parse_product_info(document)

    review_div = document.find(**current_app.config["FILTERS_FOR"]["review_block"])

    if not review_div:
        return (reviews, "", product)

    reviews_tag = review_div.find_all(**current_app.config["FILTERS_FOR"]["review"])

    review_parser = ReviewParser()
    for review in reviews_tag:
        reviews.append(review_parser.parse(review))

    next_location = document.find(**current_app.config["FILTERS_FOR"]["next_location"])

    if not next_location:
        return (reviews, "", product)

    return (reviews, next_location["href"], product)

def _parse_product_info(from_):
    product = Product()

    name_tag = from_.find(**current_app.config["FILTERS_FOR"]["name"])

    if name_tag:
        product.name = name_tag.text.strip()
    
    avg_score_tag = from_.find(**current_app.config["FILTERS_FOR"]["score"])
    if avg_score_tag:
        product.avg_score = float(avg_score_tag["content"].strip())
    
    review_count_tag = from_.find(**current_app.config["FILTERS_FOR"]["review_count"])
    if review_count_tag:
        span = review_count_tag.find("span")
        if span:
            product.review_count = int(span.text.strip())
    
    return product

def _get_tag(from_, filter):
    return from_.find(**current_app.config["FILTERS_FOR"][filter])