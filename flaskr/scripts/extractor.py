from flask import current_app, url_for
from bs4 import BeautifulSoup

import httpx

from .review_parser import ReviewParser

from ..scripts.utils import convert_to_csv, convert_to_xlsx, ensure_dir_exists, escape_string, write_json_str
from ..models.product import Product


async def save_review_to_file(product_id):
    reviews, product = await _fetch_product_info(product_id)
    
    ensure_dir_exists("./products/")
    ensure_dir_exists("./reviews/")

    write_json_str(f"./products/{product_id}.json", product.to_json_str())
    write_json_str(f"./reviews/{product_id}.json", f"[{','.join(rev.to_json_str() for rev in reviews)}]")
    
    csv_destination = f"./reviews/{product_id}.csv"
    convert_to_csv(reviews, csv_destination)
    convert_to_xlsx(csv_destination, f"./reviews/{product_id}.xlsx")


def _finish_product(product, product_id, reviews):
    product.id = product_id
    product.review_count = len(reviews)

    for review in reviews:
        product.pros_count += len(review.pros)
        product.cons_count += len(review.cons)

    product.json_url = url_for("product.download", product_id=product_id, ext="json")
    product.csv_url = url_for("product.download", product_id=product_id, ext="csv")
    product.xlsx_url = url_for("product.download", product_id=product_id, ext="xlsx")
    

async def _fetch_product_info(product_id):
    base_url = "https://www.ceneo.pl"
    location = f"/{product_id}#tab=reviews"

    reviews = []
    product = None
    is_first_page = True
    page = 1

    async with httpx.AsyncClient(**current_app.config["HTTP_CONFIG"]) as client:
        while page <= 50:
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

    _finish_product(product, product_id, reviews)

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


def _parse_product_info(document):
    product = Product()

    name_tag = document.find(**current_app.config["FILTERS_FOR"]["name"])

    if name_tag:
        product.name = escape_string(name_tag.text).strip()
    
    avg_score_tag = document.find(**current_app.config["FILTERS_FOR"]["score"])
    if avg_score_tag:
        product.avg_score = float(avg_score_tag["content"].strip())
    
    return product
