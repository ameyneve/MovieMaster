# coding=utf-8
from src import api
from src.movies.api import Movie, Movies, SearchMovie

api.add_resource(Movie, "/movie/<pk>")
api.add_resource(SearchMovie, "/movie/search/<name>")
api.add_resource(Movies, "/movies")
