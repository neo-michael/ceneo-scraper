import markdown

from flask import current_app, request, session
from os import path


def mark2html(markdown_file, locale):
    localized_file = f"{markdown_file}-{locale}.md"

    if path.isfile(localized_file):
        markdown_file = localized_file
    else:
        markdown_file = f"{markdown_file}.md"

    with open(markdown_file, "r", encoding="utf-8") as md_fp:
        md_contents = md_fp.read()

    return markdown.markdown(md_contents)

def read_json_str(file_path):
    with open(file_path, 'r', encoding="utf-8") as fp:
        return fp.read().replace('"', r'\"')
    

def get_locale():
    if "lang" in request.cookies:
        return request.cookies.get("lang")
    
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])