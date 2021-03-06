from os import getenv
import redis

class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_ENGINE_OPTIONS = {
    'echo': True,
    'pool_size': 10,
    'max_overflow': 10,
    'pool_recycle': 3600,
    'pool_timeout': 10,
    'pool_pre_ping': True
    }
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url(getenv('REDIS_URL'))

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

   
    