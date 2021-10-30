from os import getenv

class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')

class devConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')

    
class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    DEBUG = False
    TESTING = False

   
    