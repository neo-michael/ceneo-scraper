from flask import current_app, request
from pathlib import Path
from os import path

import markdown
import pandas
import json
import csv


def mark2html(markdown_file, locale):
    localized_file = f"{markdown_file}-{locale}.md"

    if path.isfile(localized_file):
        markdown_file = localized_file
    else:
        markdown_file = f"{markdown_file}.md"

    with open(markdown_file, "r", encoding="utf-8") as md_fp:
        md_contents = md_fp.read()

    return markdown.markdown(md_contents)


def ensure_dir_exists(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)


def read_json_str(file_path):
    with open(file_path, 'r', encoding="utf-8") as fp:
        return fp.read().replace('"', r'\"')


def read_json(file_path):
    with open(file_path, 'r', encoding="utf-8") as fp:
        return json.load(fp)


def write_json_str(file_path, data):
    with open(file_path, 'w') as fp:
        fp.write(data)


def convert_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        if len(data) == 0:
            return
        
        header = data[0].__dict__.keys()
        writer.writerow(header)

        for obj in data:
            writer.writerow(obj.__dict__.values())


def convert_to_xlsx(from_csv, to):
    read_file = pandas.read_csv(from_csv)
    read_file.to_excel(to, index=None, header=True)


def get_locale():
    if "lang" in request.cookies:
        return request.cookies.get("lang")
    
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])



CONTROL_CHARACTERS = ''.join(chr(i) for i in range(32))
ESCAPE_TABLE = str.maketrans({
    '"': '\u201c',
    "'": '\u201c',
    **{ char: None for char in CONTROL_CHARACTERS } 
})

def escape_string(text):
    return text.translate(ESCAPE_TABLE)
