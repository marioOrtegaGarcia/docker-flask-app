"""
    __init__.py
        - Imports Flask
        - Creates the app callable object
"""
import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.debug = True
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.secret_key = os.environ['APP_SECRET_KEY']
bs = Bootstrap(app)

from project import views
from project import admin_views
