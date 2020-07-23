# coding=utf-8
from flask import Flask

from src.config import Config
from src.extensions import api, jwt, db
from .accounts.urls import *


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
