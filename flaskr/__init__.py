import os
import json

from flask import Flask
from flask import make_response, redirect, render_template, request, session, url_for

from flask_babel import Babel

from .scripts.utils import get_locale


def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    babel = Babel(app, locale_selector=get_locale)

    # Route index to the correct view
    @app.route("/", methods=("GET",))
    def index():
        return redirect(url_for("description.index"))

    @app.route("/set_language/<location>", methods=("POST",))
    def set_language(location):
        # Python's json library expexts double quotes instead of single :(
        args = request.form["args"].replace("'", '"')
        response = make_response(redirect(url_for(location, **json.loads(args))))

        lang = request.form["lang"]
        response.set_cookie("lang", lang)
        return response
    
    from . import description_blueprint
    from . import product_blueprint

    app.register_blueprint(description_blueprint.bp)
    app.register_blueprint(product_blueprint.bp)

    app.jinja_env.globals.update(get_locale=get_locale)
    app.jinja_env.globals.update(get_locales=lambda: app.config["LANGUAGES"])
    
    return app
