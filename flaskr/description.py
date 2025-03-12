from flask import Blueprint
from flask import make_response, redirect, render_template, request, url_for

from .scripts.utils import mark2html, get_locale

bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    return render_template("description/index.html", text=mark2html("./ABOUT", get_locale()))

@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html")

# @bp.route("/", methods=("GET", "POST"))
@bp.route("/<file_name>", methods=("GET", "POST"))
def handle_file(file_name):
    # if not file_name and "last_file" in request.cookies:
    #     print("TEST")
    #     file_name = request.cookies["last_file"]
    # not file_name or
    if file_name == "libraries":
        libs = []
        with open("requirements.txt", 'r') as fp:
            for line in fp:
                (name, version) = line.split("==")
                libs.append(name
        )
        return render_template("description/index.html", text=render_template("description/libraries.html", libs=libs))

    if not file_name in ("README.md", "WIKI.md"):
        return redirect(url_for("description.index"))
    
    # html = render_template("description/index.html", text=mark2html(file_name[:-3], get_locale()))
    # if file_name:
    #     response = make_response(html)
    #     response.set_cookie("last_file", file_name)
    #     return response
    
    return render_template("description/index.html", text=mark2html(file_name[:-3], get_locale()))
