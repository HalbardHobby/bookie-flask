from os import name
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    isbn = db.Column(db.String(20))
    year = db.Column(db.Integer)
    summary= db.Column(db.Text)