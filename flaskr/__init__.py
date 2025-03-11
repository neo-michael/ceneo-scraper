import os

from flask import Flask
from flask import render_template, redirect, url_for, session, request, make_response

from .scripts.utils import get_locale, get_other_locale

from flask_babel import Babel

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    
    babel = Babel(app, locale_selector=get_locale)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Route index to the correct view
    @app.route("/", methods=("GET",))
    def index():
        return redirect(url_for("description.index"))

    @app.route("/set_language/<location>", methods=("POST",))
    def set_language(location):
        response = make_response(redirect(url_for(location)))
        lang = request.form["lang"]
        response.set_cookie("lang", lang)
        return response
    
    from . import description
    from . import product

    app.register_blueprint(description.bp)
    app.register_blueprint(product.bp)


    app.jinja_env.globals.update(get_locale=get_locale)
    app.jinja_env.globals.update(get_locales=lambda: app.config["LANGUAGES"])
    
    return app
