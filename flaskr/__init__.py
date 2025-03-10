import os

from flask import Flask
from flask import render_template, redirect, url_for


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Route index to the correct view
    @app.route('/')
    def index():
        return redirect(url_for("description.index"))


    from . import description
    app.register_blueprint(description.bp)

    from . import product
    app.register_blueprint(product.bp)

    return app
