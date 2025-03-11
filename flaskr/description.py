from flask import Blueprint
from flask import render_template

bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    return render_template("description/index.html")

@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html")