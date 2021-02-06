# import os
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite3')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
# ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
# TESTING = True
#

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = 'username'
ADMIN_PASSWORD = 'Password'
SECRET_KEY = ''

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_USE_TLS = False
MAIL_USE_SSL = True
