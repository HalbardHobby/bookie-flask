from os import name
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "book"
    
    id = db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = db.Column('name', db.Text, nullable=False)
    author = db.Column('author', db.Text, nullable=False)
    isbn = db.Column('isbn', db.String(20))
    year = db.Column('year', db.Integer)
    summary= db.Column('summary', db.Text)