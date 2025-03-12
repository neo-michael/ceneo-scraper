from flask import Blueprint
from flask import render_template, redirect, request, url_for, make_response

from os import path
from flask_babel import _

from .scripts import extractor


bp = Blueprint("product", __name__, url_prefix="/product")

@bp.route("/product_list", methods=("GET",))
def product_list():
    return render_template("product/product_list.html")


@bp.route("/extract", methods=("GET", "POST"))
async def extract():
    if request.method == "GET":
        return render_template("product/extract.html")

    elif request.method == "POST":
        product_id = request.form.get("product_id", default="")

        if not is_valid_product_id(product_id):
            return render_template(
                "product/extract.html",
                error_message=_("Product id should only contain digits."),
            )
        review_file = f"reviews/{product_id}.json"
        if not path.isfile(review_file):
            await extractor.save_reviews_to_json(product_id)

        return redirect(url_for("product.product", product_id=product_id))

    return render_template(
        "product/extract.html",
        error_message=_("Unexpected error occured. Please report it to the site owner."),
    )


@bp.route("/<product_id>", methods=("GET", ))
def product(product_id):

    with open(f"./reviews/{product_id}.json", encoding="utf-8") as fp:
        reviews = fp.read()

    return render_template("product/product.html", reviews=reviews.replace('\n', '\\\n').replace('"', r'\"').replace('\\n', '\\\\n'))


def is_valid_product_id(str):
    return str.isdigit()
