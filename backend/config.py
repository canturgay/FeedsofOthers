from os import getenv

class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')

class devConfig(Config):
    TESTING = True
    DEBUG = True

class testConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv('TEST_DATABASE_URI')
    DEBUG = True
    

class stageConfig(Config):
    TESTING = True
    DEBUG = True

    
class prodConfig(Config):
    DEBUG = False
    TESTING = False

   
    