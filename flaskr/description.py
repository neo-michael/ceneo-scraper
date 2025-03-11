from flask import Blueprint
from flask import render_template, redirect, url_for

from .scripts.utils import mark2html


bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    return render_template("description/index.html", text=mark2html("./ABOUT.md"))

@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html")

@bp.route("<file_name>", methods=("GET", ))
def handle_file(file_name):
    if not file_name == "README.md":
        return redirect(url_for("description.index"))
    
    return render_template("description/index.html", text=mark2html("./README.md"))
