# coding=utf-8

from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy import asc

from src import db
from src.accounts.permissions import admin_required
from src.decorators import gzipped
from src.movies.models import MovieModel

parser = RequestParser()
parser.add_argument("99popularity", type=str, required=True)
parser.add_argument("director", type=str, required=True)
parser.add_argument('genre', type=str, action="append")
parser.add_argument("imdb_score", type=float, required=True)
parser.add_argument("name", type=str, required=True)


class SearchMovie(Resource):
    def get(self, name):
        movies = MovieModel.query.filter(MovieModel.name.ilike(f"%{name}%"))
        if not movies:
            return {"message": f"Could not find {name}"}
        result = list()
        for movie in movies:
            result.append(movie.to_json())
        return result


class Movie(Resource):
    @admin_required
    def put(self, pk):
        movie = MovieModel.find_by_id(pk)
        if not movie:
            return {"message": f"Could not find movie with ID: {pk}"}

        args = parser.parse_args()
        movie.name = args['name']
        movie.popularity = args['99popularity']
        movie.director = args['director']
        movie.imdb_score = args['imdb_score']
        movie.genre = args['genre']
        db.session.commit()
        return {"message": f"Movie {movie.name} details updated successfully"}

    @admin_required
    def delete(self, pk):
        movie = MovieModel.find_by_id(pk)
        if not movie:
            return {"message": f"Could not find movie with ID: {pk}"}

        db.session.delete(movie)
        db.session.commit()
        return {"message": f"Movie deleted successfully"}


class Movies(Resource):
    @gzipped
    def get(self):
        all_movies = list()
        movies = MovieModel.query.order_by(asc(MovieModel.id)).all()
        for movie in movies:
            all_movies.append(movie.to_json())
        return all_movies

    @admin_required
    def post(self):
        args = parser.parse_args()

        movie = MovieModel(
            name=args["name"],
            popularity=args["99popularity"],
            director=args["director"],
            imdb_score=args["imdb_score"],
            genre=args["genre"]
            )
        db.session.add(movie)
        db.session.commit()

        return {"message": f"Movie {args['name']} added successfully with ID: {movie.id}"}, 201
