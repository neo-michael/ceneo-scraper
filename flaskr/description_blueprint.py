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
    
    delim_pos = file_name.find('.')
    dash_pos = file_name.find('-')
    if not dash_pos == -1 and dash_pos < delim_pos:
        delim_pos = dash_pos

    if not file_name[: delim_pos] in ("README", "WIKI"):
        return redirect(url_for("description.index"))
    
    return render_template("description/index.html", text=mark2html(file_name[:delim_pos], get_locale()))
