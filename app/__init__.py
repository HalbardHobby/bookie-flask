import os

from flask import Flask
from . import books

def create_app():
    app = Flask(__name__)

    app.register_blueprint(books.bp)

    return app
