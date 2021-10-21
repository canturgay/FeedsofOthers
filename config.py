class Config(object):
    TESTING = False
    DEBUG = False

class devConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True
    DB_SERVER = 'localserver'
    DATABASE_URI = ''
    

class testConfig(Config):
    DB_SERVER = ''
    DATABASE_URI = ''
    DEBUG = False
    TESTING = True