#!/usr/bin/env python

import os

from flask import Flask, render_template
from flask_webpack import Webpack

webpack = Webpack()

def create_app(settings_override=None):

    app_dir = os.path.dirname(__file__)
    build_dir = os.path.join(os.path.abspath(os.path.join(app_dir, os.pardir)), 'build')

    app = Flask(__name__)
    app.config.update({'WEBPACK_MANIFEST_PATH': os.path.join(build_dir, 'manifest.json')})

    if settings_override:
        app.config.update(settings_override)

    webpack.init_app(app)

    return app

app = create_app()


@app.route("/")
def hello():
    return render_template('index.html', title="notes!!!")
