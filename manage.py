#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append("script")

import myflask
from flask import render_template
from flask_bootstrap import Bootstrap

app = myflask.MyFlask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()