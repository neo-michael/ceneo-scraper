from flask import Blueprint
from flask import redirect, render_template, request, url_for

from .scripts.utils import mark2html, get_locale

bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    return render_template("description/index.html", text=mark2html("./ABOUT", get_locale()))

@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html")

@bp.route("<file_name>", methods=("GET", ))
def handle_file(file_name):
    if not file_name in ("README.md", "WIKI.md"):
        return redirect(url_for("description.index"))
    
    return render_template("description/index.html", text=mark2html(file_name[:-3], get_locale()))
