#!/usr/bin/env python

from os import path, pardir

from flask import Flask, render_template, send_from_directory
from flask_webpack import Webpack

APP_DIR = path.dirname(__file__)
BUILD_DIR = path.join(path.abspath(path.join(APP_DIR, pardir)), 'build')

webpack = Webpack()

def create_app(settings_override=None):

    app = Flask(__name__)
    app.config.update({'WEBPACK_MANIFEST_PATH': path.join(BUILD_DIR, 'manifest.json')})

    if settings_override:
        app.config.update(settings_override)

    webpack.init_app(app)

    return app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html', title='notes!!!')

@app.route('/notes')
def notes():
    return render_template('notes.html', title='notes!!!')

# # without webpack you could serve static files like this for development
# # either way, in production its best to let nginx or the main webserver serve them
# @app.route('/assets/<path:filename>')
# def send_asset(filename):
#     return send_from_directory(path.join(APP_DIR, 'assets'), filename)
