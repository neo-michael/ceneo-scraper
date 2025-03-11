from flask import Blueprint
from flask import render_template

import markdown

bp = Blueprint("description", __name__, url_prefix="/description")


@bp.route("/index", methods=("GET",))
def index():
    with open("./ABOUT.md", 'r', encoding="utf-8") as md_fp:
        md_contents = md_fp.read()
    
    html = markdown.markdown(md_contents)
    print(html)
    return render_template("description/index.html", text=html)

@bp.route("/about", methods=("GET",))
def about():
    return render_template("description/about.html")