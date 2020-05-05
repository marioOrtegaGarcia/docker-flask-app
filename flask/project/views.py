"""
    views.py
        - Views is used to mange all of our app routes
"""
import os
import datetime
import hashlib as hash

from flask import render_template, redirect, url_for, request, flash
from project import app


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "About"
