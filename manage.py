#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template
from flask import Flask
from flask import globals

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def index(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()