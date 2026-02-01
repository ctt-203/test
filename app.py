#!/usr/bin/env python
# coding: utf-8
import flask
import string

app = flask.Flask(__name__)

@app.route("/hello/<name>")
def index(name):
    return flask.render_template("template.txt", name=name)