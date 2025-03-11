from flask import request, current_app, session
from os import path

import markdown


def mark2html(markdown_file, locale):
    localized_file = f"{markdown_file}-{locale}.md"

    if path.isfile(localized_file):
        markdown_file = localized_file
    else:
        markdown_file = f"{markdown_file}.md"

    with open(markdown_file, "r", encoding="utf-8") as md_fp:
        md_contents = md_fp.read()

    return markdown.markdown(md_contents)

def get_locale():
    if "lang" in request.cookies:
        return request.cookies.get("lang")
    
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])

def get_other_locale():
    current_loc = get_locale()

    for loc in current_app.config["LANGUAGES"]:
        if not loc == current_loc:
            return loc
    return "en"