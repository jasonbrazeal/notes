#!/usr/bin/env python

import os
from os import pardir
from pathlib import Path
import mimetypes
import json
from datetime import datetime

from flask import Flask, render_template, send_from_directory, jsonify, request, Response, Markup
from flask_webpack import Webpack

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from pygments import highlight
from pygments.lexers import PythonLexer, RubyLexer, JavascriptLexer, HtmlLexer, CssLexer
from pygments.formatters import HtmlFormatter


APP_DIR = os.path.dirname(__file__)
BUILD_DIR = os.path.join(os.path.abspath(os.path.join(APP_DIR, pardir)), 'build')
NOTES_DIR = '/Users/jsonbrazeal/Dropbox/Notes'

def create_app(settings_override=None):
    webpack = Webpack()
    app = Flask(__name__, static_folder=NOTES_DIR)
    app.config.update({'WEBPACK_MANIFEST_PATH': os.path.join(BUILD_DIR, 'manifest.json')})
    if settings_override:
        app.config.update(settings_override)
    webpack.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', title='notes!!!')

@app.route('/notes/<path:relpath>/')
@app.route('/notes/', defaults={'relpath': ''})
def notes(relpath):
    # import time;time.sleep(4)
    notes = get_notes(relpath)
    if notes:
        # directory:
        notes = notes['children']
        # file:
        if notes is None:
            filename = Path(relpath).parts[-1]
            abspath = os.path.join(NOTES_DIR, relpath)
            _, file_extension = os.path.splitext(relpath)
            if file_extension == '.md':
                with open(abspath, mode='r', encoding='utf-8') as f:
                    html = markdown.markdown(f.read(), output_format='html5', extensions=[GithubFlavoredMarkdownExtension()])
                return render_template('content_container.html', content=Markup(html))
            elif file_extension in ('.py', '.rb', '.js', '.html', '.css'):
                if file_extension == '.py':
                    lexer = PythonLexer()
                elif file_extension == '.rb':
                    lexer = RubyLexer()
                elif file_extension == '.js':
                    lexer = JavascriptLexer()
                elif file_extension == '.html':
                    lexer = HtmlLexer()
                elif file_extension == '.css':
                    lexer = CssLexer()
                with open(abspath, mode='r', encoding='utf-8') as f:
                    html = highlight(f.read(), lexer, HtmlFormatter())
                return render_template('content_container.html', content=Markup(html))
            else:
                file_mime = mimetypes.guess_type(abspath)[0]
                if file_mime in (None, 'text/html'):
                    file_mime = 'text/plain'
                return send_from_directory(directory=Path(abspath).parent, filename=filename, mimetype=file_mime)
            return send_from_directory(directory=Path(abspath).parent, filename=filename, mimetype='text/plain')
    else:
        notes = [{'name': 'path not found'}]
    if request_wants_json(request):
        # return jsonify(notes)
        path_links = {}
        for i, d in enumerate(relpath.split('/')):
            path_links[d] = ''.join([f'/{folder}' for folder in relpath.split('/')[:(i + 1)]])
        response = app.response_class(
            response=json.dumps({'notes': notes, 'path_links': path_links}),
            status=200,
            mimetype='application/json',
        )
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return render_template('notes.html')

# # without webpack you could serve static files like this for development
# # either way, in production its best to let nginx or the main webserver serve them
# @app.route('/assets/<path:filename>')
# def send_asset(filename):
#     return send_from_directory(path.join(APP_DIR, 'assets'), filename)

from inspect import getouterframes, currentframe
def get_notes(root_path):
    if root_path is None:
        root_path = NOTES_DIR
        relpath = '/'
    else:
        root_path = os.path.join(NOTES_DIR, root_path)
        relpath = root_path
    if not Path(root_path).exists:
        return None
    IGNORE = ['.DS_Store']
    def ls_R(path_str):
        recursion_depth = len(getouterframes(currentframe()))
        path = Path(path_str)
        notes = {'name': path.parts[-1],
                 'path': path_str,
                 'relpath': str(path.relative_to(NOTES_DIR))}
        if path.is_dir():
            # print('  ' * recursion_depth + 'directory: {}'.format(path))
            notes.update({'type': 'dir',
                          'children': [ls_R(str(item)) for item in Path(path).iterdir() if item.parts[-1] not in IGNORE]
                         })
        elif path.is_file():
            # print('  ' * recursion_depth + 'file: {}'.format(path))
            notes.update({'type': 'file',
                          'children': None})
        else:
            # print('  ' * recursion_depth + 'unkown: {}'.format(path))
            # print('passing on that ^^^')
            return
        return notes

    return ls_R(root_path)

def request_wants_json(request):
    best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
    return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']
