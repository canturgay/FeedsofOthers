class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class devConfig(Config):
    TESTING = True
    
    
class prodConfig(Config):
    pass