from flask import Blueprint
from .db import db, Book

bp = Blueprint('books', __name__, url_prefix=None)

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def list_boooks():
    return Book.query.all()[0].isbn

@bp.route('/', methods=['POST'])
def create_book(book_id):
    return "create book"

@bp.route('/<book_id>', methods=['GET'])
def read_book(book_id):
    return "book info" + book_id

@bp.route('/<book_id>', methods=['PUT'])
def update_book(book_id):
    return "book updated" + book_id

@bp.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return "book deleted" + book_id