import os

from flask import Flask
from . import books

def create_app():
    app = Flask(__name__)

    app.register_blueprint(books.bp)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app
