# coding=utf-8
from src import api
from src.movies.api import Movie, Movies

api.add_resource(Movie, "/movie/<name>")
api.add_resource(Movies, "/movies")
