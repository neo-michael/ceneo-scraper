from flask import Blueprint
from flask import render_template

bp = Blueprint("product", __name__, url_prefix='/product')


@bp.route("/product_list", methods=("GET",))
def product_list():
    return render_template('product/product_list.html')

@bp.route("/extract", methods=("GET", "POST"))
def extract():
    return render_template('product/extract.html')