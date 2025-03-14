import httpx
import json

from bs4 import BeautifulSoup
from flask import current_app, url_for

from ..models.product import Product
from .review_parser import ReviewParser
from ..scripts.utils import convert_to_csv, convert_to_xlsx


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
    product = Product() if is_first_page else None

    document = BeautifulSoup(contents, "lxml")

    if is_first_page:
        name_tag = document.find("div", class_="js_searchInGoogleTooltip breadcrumbs__item")

        if name_tag:
            product.name = name_tag.text.strip()
        
        avg_score_tag = document.find("span", class_="product-review__score", content=True)
        if avg_score_tag:
            product.avg_score = float(avg_score_tag["content"].strip())
        
        review_count_tag = document.find("a", class_="product-review__link link link--accent js_reviews-link js_clickHash js_seoUrl")
        if review_count_tag:
            span = review_count_tag.find("span")
            if span:
                product.review_count = int(span.text.strip())

    review_div = document.find(
        "div", class_="js_product-reviews js_reviews-hook js_product-reviews-container"
    )

    if not review_div:
        return (reviews, "", product)

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
        return (reviews, "", product)

    return (reviews, next_location["href"], product)