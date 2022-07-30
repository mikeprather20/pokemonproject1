import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://jtixhqdb:HhxtRX_uhGHHi79KxqgAJEJ1zCQMTt5A@queenie.db.elephantsql.com/jtixhqdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False