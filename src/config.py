# coding=utf-8
import datetime
import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_IDENTITY_CLAIM = 'sub'
    JWT_USER_CLAIMS = 'payload'

    BUNDLE_ERRORS = True

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=10)
