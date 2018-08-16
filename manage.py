#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()