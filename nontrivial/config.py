import os
class Config(object):

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
MSEARCH_INDEX_NAME = 'msearch'
MSEARCH_BACKEND = 'whoosh'
MSEARCH_ENABLE = True
