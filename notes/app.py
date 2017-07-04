#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title="notes!!!")

if __name__ == "__main__":
    app.run()
