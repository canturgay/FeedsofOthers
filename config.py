import os

class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class devConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    
    
class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    TESTING = False
    