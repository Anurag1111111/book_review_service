
from flask_restful import Api, Resource, reqparse
from app.models import Book, Review
from app.db import db
from app.cache import get_books_cache, set_books_cache
from flasgger import swag_from

api = Api()

book_parser = reqparse.RequestParser()
book_parser.add_argument("title", type=str, required=True)

review_parser = reqparse.RequestParser()
review_parser.add_argument("content", type=str, required=True)

class BookListResource(Resource):
    @swag_from("docs/books/get_books.yml")
    def get(self):
        cached = get_books_cache()
        if cached:
            return cached, 200
        books = Book.query.all()
        result = [{"id": b.id, "title": b.title} for b in books]
        set_books_cache(result)
        return result, 200

    @swag_from("docs/books/post_book.yml")
    def post(self):
        args = book_parser.parse_args()
        book = Book(title=args["title"])
        db.session.add(book)
        db.session.commit()
        return {"id": book.id, "title": book.title}, 200


class ReviewResource(Resource):
    @swag_from("docs/reviews/get_reviews.yml")
    def get(self, book_id):
        reviews = Review.query.filter_by(book_id=book_id).all()
        return [{"id": r.id, "content": r.content} for r in reviews], 200

    @swag_from("docs/reviews/post_review.yml")
    def post(self, book_id):
        args = review_parser.parse_args()
        review = Review(content=args["content"], book_id=book_id)
        db.session.add(review)
        db.session.commit()
        return {"id": review.id, "content": review.content}, 200


api.add_resource(BookListResource, '/books')
api.add_resource(ReviewResource, '/book/<int:book_id>/reviews')
