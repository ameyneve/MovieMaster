# coding=utf-8
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from src import db
from src.accounts.permissions import admin_required
from src.movies.models import MovieModel

parser = RequestParser()
parser.add_argument("99popularity", type=str, required=True)
parser.add_argument("director", type=str, required=True)
parser.add_argument('genre', type=str, action="append")
parser.add_argument("imdb_score", type=float, required=True)
parser.add_argument("name", type=str, required=True)


class Movie(Resource):
    def get(self, name):
        movie = MovieModel.find_by_name(name)
        if not movie:
            return {"message": f"Could not find {name}"}
        return movie.to_json()

    @admin_required
    def put(self, name):
        movie = MovieModel.find_by_name(name)
        if not movie:
            return {"message": f"Could not find {name}"}

        args = parser.parse_args()
        movie.name = args['name']
        movie.popularity = args['99popularity']
        movie.director = args['director']
        movie.imdb_score = args['imdb_score']
        movie.genre = args['genre']
        db.session.commit()
        return {"message": f"Movie {name} details updated successfully"}

    @admin_required
    def delete(self, name):
        movie = MovieModel.find_by_name(name)
        if not movie:
            return {"message": f"Could not find {name}"}

        db.session.delete(movie)
        db.session.commit()
        return {"message": f"Movie {name} deleted successfully"}


class Movies(Resource):
    def get(self):
        all_movies = list()
        movies = MovieModel.query.all()
        for movie in movies:
            all_movies.append(movie.to_json())
        return all_movies

    @admin_required
    def post(self):
        args = parser.parse_args()

        if MovieModel.find_by_name(args['name']):
            return {"message": f"Movie {args['name']} already exists"}

        movie = MovieModel(
            name=args["name"],
            popularity=args["99popularity"],
            director=args["director"],
            imdb_score=args["imdb_score"],
            genre=args["genre"]
            )
        db.session.add(movie)
        db.session.commit()

        return {"message": f"Movie {args['name']} added successfully"}, 201
