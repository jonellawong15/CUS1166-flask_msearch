import os
class Config(object):

DEBUG = True
SQLALCHEMY_DATABASE_URI = user='wongjonella', password='password',
                              host='127.0.0.1:3306',
                              database='flaskproj'
MSEARCH_INDEX_NAME = 'msearch'
MSEARCH_BACKEND = 'whoosh'
MSEARCH_ENABLE = True
