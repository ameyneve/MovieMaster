# coding=utf-8
import datetime


class Config:
    SQLALCHEMY_DATABASE_URI = "postgres://mpxagonyiygeoa:6dd6dd18c6a437c48483177f2dfcb4f45555208c70fa57552876b6b37379c537@ec2-3-216-129-140.compute-1.amazonaws.com:5432/dbkgmifuq43pbo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some-secret-string'
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_IDENTITY_CLAIM = 'sub'
    JWT_USER_CLAIMS = 'payload'

    BUNDLE_ERRORS = True

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=10)
