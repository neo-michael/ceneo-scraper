from flask import redirect, render_template, url_for
from flask import Blueprint

from .scripts.utils import mark2html, get_locale

bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    return render_template("description/index.html", text=mark2html("./ABOUT", get_locale()))


@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html", text=mark2html("./AUTHOR", get_locale()))


@bp.route("/<file_name>", methods=("GET", "POST"))
def handle_file(file_name):
    if file_name == "libraries":
        libs = []
        with open("requirements.txt", 'r') as fp:
            for line in fp:
                (name, version) = line.split("==")
                libs.append(name)

        return render_template("description/index.html", text=render_template("description/libraries.html", libs=libs))

    if not file_name in ("README.md", "WIKI.md"):
        return redirect(url_for("description.index"))
    
    return render_template("description/index.html", text=mark2html(file_name[:-3], get_locale()))
