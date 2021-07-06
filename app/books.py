from flask import Blueprint, request, jsonify
from .db import db, Book

bp = Blueprint('books', __name__, url_prefix=None)

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def list_boooks():
    res = []
    for r in Book.query.all():
        res.append(r.to_dict())
    return jsonify(res), 200

@bp.route('/', methods=['POST'])
def create_book():

    return "create book"

@bp.route('/<book_id>', methods=['GET'])
def read_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    response = (jsonify(book.to_dict()), 200) if book is not None else ({}, 404)
    return response

@bp.route('/<book_id>', methods=['PUT'])
def update_book(book_id):
    return "book updated" + book_id

@bp.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return {}, 404
    else:
        db.session.delete(book)
        db.session.commit()
        return {}, 204
