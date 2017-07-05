#!/usr/bin/env python

from os import path, pardir

from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_webpack import Webpack

APP_DIR = path.dirname(__file__)
BUILD_DIR = path.join(path.abspath(path.join(APP_DIR, pardir)), 'build')
NOTES_DIR = '/Users/jsonbrazeal/Dropbox/Notes'

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
    if request_wants_json(request):
        return jsonify(get_notes())
    return render_template('notes.html', title='notes!!!')

# # without webpack you could serve static files like this for development
# # either way, in production its best to let nginx or the main webserver serve them
# @app.route('/assets/<path:filename>')
# def send_asset(filename):
#     return send_from_directory(path.join(APP_DIR, 'assets'), filename)

from pathlib import Path
from inspect import getouterframes, currentframe
def get_notes(base_path=NOTES_DIR):
    IGNORE = ['.DS_Store']
    def ls_R(path_str):
        recursion_depth = len(getouterframes(currentframe()))
        path = Path(path_str)
        notes = {'name': path.parts[-1],
                 'path': str(path)}
        if path.is_dir():
            print('  ' * recursion_depth + 'directory: {}'.format(path))
            notes.update({'type': 'dir',
                          'children': [ls_R(str(item)) for item in Path(path).iterdir() if item.parts[-1] not in IGNORE]
                         })
        elif path.is_file():
            print('  ' * recursion_depth + 'file: {}'.format(path))
            notes.update({'type': 'file',
                          'children': None})
        else:
            print('  ' * recursion_depth + 'unkown: {}'.format(path))
            print('passing on that ^^^')
            return
        return notes

    return ls_R(base_path)

def request_wants_json(request):
    best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
    print(best)
    return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']
