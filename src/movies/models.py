# coding=utf-8
from sqlalchemy.types import ARRAY

from src import db


class MovieModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    popularity = db.Column(db.Integer)
    director = db.Column(db.String(120))
    imdb_score = db.Column(db.Float(precision=2))
    genre = db.Column(ARRAY(db.String))

    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "99popularity": self.popularity,
            "director": self.director,
            "imdb_score": self.imdb_score,
            "genre": self.genre
            }
        return data

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)
