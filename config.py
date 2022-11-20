import os

FLASK_APP = "app.py"
ENV = "development"
DEBUG = True
SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost:3306/test?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_ECHO = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

BASE_DIR = os.path.dirname(__file__)
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = 'INFO'

DOC_DIR = os.path.join(BASE_DIR, 'docs')
