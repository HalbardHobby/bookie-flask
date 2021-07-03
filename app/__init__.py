import os
from flask import Flask
from .db import db

from . import books

db_uri = "postgresql://"+ os.environ["DB_USERNAME"] + ":" + \
        os.environ["DB_PASSWORD"] + "@" + os.environ["DB_HOST"] + \
        ":5432/postgres"

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)
    app.register_blueprint(books.bp)

    return app
