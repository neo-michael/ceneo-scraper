from flask import render_template, redirect, request, send_file, url_for
from flask import Blueprint
from flask_babel import _
from os import path

import glob
import os

from .scripts.utils import read_json, read_json_str
from .scripts import extractor


bp = Blueprint("product", __name__, url_prefix="/product")


@bp.route("/product_list", methods=("GET",))
def product_list():
    prod_list = []

    for product_file in glob.glob("./products/*.json"):
        prod_list.append(read_json_str(product_file))

    prod_list_as_str = f"[{','.join(prod_list)}]"
    return render_template("product/product_list.html", products=prod_list_as_str)


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
            await extractor.save_review_to_file(product_id)

        return redirect(url_for("product.product", product_id=product_id))

    return render_template(
        "product/extract.html",
        error_message=_(
            "Unexpected error occured. Please report it to the site owner."
        ),
    )


@bp.route("/<product_id>", methods=("GET",))
def product(product_id):
    reviews = read_json_str(f"./reviews/{product_id}.json")
    product_info = read_json(f"./products/{product_id}.json")

    return render_template(
        "product/product.html",
        reviews=reviews,
        urls={
            "JSON": product_info["json_url"],
            "CSV": product_info["csv_url"],
            "XLSX": product_info["xlsx_url"],
        },
        name=product_info["name"],
    )


@bp.route("/charts/<product_id>", methods=("GET",))
def charts(product_id):
    reviews = read_json_str(f"./reviews/{product_id}.json")
    product_info = read_json(f"./products/{product_id}.json")

    return render_template(
        f"product/charts.html", reviews=reviews, name=product_info["name"]
    )


@bp.route("/<product_id>/<ext>", methods=("GET",))
def download(product_id, ext):
    return send_file(f"../reviews/{product_id}.{ext}", as_attachment=True)


@bp.route("/delete/<product_id>", methods=("GET",))
def delete(product_id):
    os.remove(f"./reviews/{product_id}.json")
    os.remove(f"./reviews/{product_id}.csv")
    os.remove(f"./reviews/{product_id}.xlsx")
    os.remove(f"./products/{product_id}.json")

    return redirect(url_for("product.product_list"))


def is_valid_product_id(str):
    return str.isdigit()
