from flask_httpauth import HTTPTokenAuth

from app.server.db.models import AuthToken

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    """Used to verify user's Token"""
    return AuthToken.query.filter_by(auth_token=token).first()

