# ------- standard library imports -------
import random
import string
import secrets
from random import choices
from datetime import datetime

# ------- local imports -------
from sqlalchemy import ForeignKey
from .extensions import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=5))
        url = self.query.filter_by(short_url=short_url).first()

        if url:
            return self.generate_short_url()

        return short_url

    def __repr__(self):
        return f'{self.original_url}, {self.visits}'


class AuthToken(db.Model):
    __tablename__ = 'auth_token'
    id = db.Column(db.Integer, primary_key=True)
    auth_token = db.Column(db.String(16))
    date_created = db.Column(db.DateTime, default=datetime.now)
    email_id = db.Column(db.Integer, ForeignKey('email.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auth_token = self.generate_auth_token() if self.auth_token is None else self.auth_token

    @staticmethod
    def generate_auth_token():
        generated_token = secrets.token_hex(16)
        return generated_token

    def __repr__(self):
        return f'{self.auth_token}'


class Email(db.Model):
    __tablename__ = 'email'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(512), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    is_verified = db.Column(db.Boolean, default=False)
    verification_code = db.relationship('VerificationCode', backref='email')
    auth_token = db.relationship('AuthToken', backref='email')

    def __repr__(self):
        return f'{self.email}, {self.verification_code}, {self.auth_token}'


class VerificationCode(db.Model):
    __tablename__ = 'verification_code'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.Integer, ForeignKey('email.id'))
    verification_code = db.Column(db.String, unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verification_code = self.generate_verification_code()

    @staticmethod
    def generate_verification_code():
        verification_code = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        return verification_code

    def __repr__(self):
        return f'{self.verification_code}'
