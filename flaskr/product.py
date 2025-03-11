from flask import Blueprint
from flask import render_template, redirect, request, url_for


from . import extractor

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

        if is_valid_product_id(product_id):
            #await extractor.save_reviews_to_json(product_id)
            await extractor._fetch_reviews(product_id)
            return redirect(url_for("product.product", product_id=product_id), code=302)
        
        return render_template(
            "product/extract.html",
            error_message="Product id should only contain digits.",
        )

    return render_template(
        "product/extract.html",
        error_message="Unexpected error occured. Please report it to the site owner.",
    )


@bp.route("/<product_id>", methods=("GET", ))
def product(product_id):
    print(product_id)
    return ""


def is_valid_product_id(str):
    return str.isdigit()
