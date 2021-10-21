class Config(object):
    TESTING = False
    DEBUG = False

class devConfig(Config):
    TESTING = True
    DB_SERVER = 'localserver'
    DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class testConfig(Config):
    DB_SERVER = ''
    DATABASE_URI = ''
    DEBUG = False
    TESTING = True