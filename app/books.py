from flask import Blueprint, request, jsonify
from sqlalchemy.orm import session
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
    req = request.get_json()
    try:
        new_book = Book(name=req['name'], author=req['author'], isbn=req['isbn'],
                        year=req['year'], summary=req['summary'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict(), 201
    except:
        return {"message": "Bad request"}, 400

@bp.route('/<book_id>', methods=['GET'])
def read_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    response = (jsonify(book.to_dict()), 200) if book is not None else ({}, 404)
    return response

@bp.route('/<book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return {"message": "Not found"}, 404

    try:
        req = request.get_json()
        book.name = req['name']
        book.author = req['author']
        book.isbn = req['isbn']
        book.year = req['year']
        book.summary = req['summary']
        db.session.commit()

        return book.to_dict(), 200
    except:
        return {"message": "Bad request"}, 400


@bp.route('/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.filter_by(id = book_id).first()
    if book is None:
        return {}, 404
    else:
        db.session.delete(book)
        db.session.commit()
        return {}, 204
