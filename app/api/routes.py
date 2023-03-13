from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Book, book_schema, books_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/books', methods = ['POST'])
@token_required
def create_book(current_user_token):

    title = request.json['title']
    author_first_name = request.json['author_first_name']
    author_last_name = request.json['author_last_name']
    genre = request.json['genre']
    isbn = request.json['isbn']
    year_published = request.json['year_published']
    language = request.json['language']
    pages = request.json['pages']
    words = request.json['words']
    description = request.json['description']

    user_token = current_user_token.token

    book = Book(title, author_first_name, author_last_name, genre, isbn, year_published, language, pages, words, description, user_token=user_token)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods = ['GET'])
@token_required
def get_book(current_user_token):
    a_user = current_user_token.token
    books = Book.query.filter_by(user_token = a_user).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_single_book(current_user_token, id):
    book = Book.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)

# Update endpoint
@api.route('/books/<id>', methods = ['POST', 'PUT'])
@token_required
def update_book(current_user_token, id):
    book = Book.query.get(id)

    book.title = request.json['title']
    book.author_first_name = request.json['author_first_name']
    book.author_last_name = request.json['author_last_name']
    book.genre = request.json['genre']
    book.isbn = request.json['isbn']
    book.year_published = request.json['year_published']
    book.language = request.json['language']
    book.pages = request.json['pages']
    book.words = request.json['words']
    book.description = request.json['description']

    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

# Delete endpoint
@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_book(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)
