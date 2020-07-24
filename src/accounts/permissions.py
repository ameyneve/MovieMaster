# coding=utf-8
from functools import wraps

from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['is_admin']:
            return fn(*args, **kwargs)
        return {"message": 'Your are not authorized to use this API'}, 403

    return wrapper
