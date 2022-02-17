import os

SECRET_KEY = 'mySecretKey' #os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3' #os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False #os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
ADMIN_USERNAME = 'admin' #os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = 'admin' #os.environ.get('ADMIN_PASSWORD')

MAIL_SERVER = 'localhost' # os.environ.get('MAIL_SERVER')
MAIL_PORT = 25 # int(os.environ.get('MAIL_PORT'))
MAIL_USERNAME = 'user' # os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = 'password' # os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = False
MAIL_USE_SSL = True

"""
:::::::: .env file content ::::::::
SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY=randomKey

MAIL_SERVER=smtp.gmail.com
MAIL_PORT=465
MAIL_USERNAME=email@email.com
MAIL_PASSWORD=password
"""
