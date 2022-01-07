from flask import Flask, render_template, redirect, url_for
from os import getenv
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from backend.db_helpers import db
from flask_dance.contrib.twitter import twitter
from werkzeug.middleware.proxy_fix import ProxyFix
import backend.models as models
def configure_app(app):
    #configurations
    load_dotenv()
    configure = {
        "development": "backend.config.devConfig",
        "production": "backend.config.prodConfig",
        "staging": "backend.config.stageConfig",
        "testing": "backend.config.testConfig"
    }
    
    #Determine the configuration file to read using environment variables
    config_name = getenv('FLASK_CONFIGURATION', 'development')
    #Read settings as objects
    app.config.from_object(configure[config_name])
    return app.config

def create_app():
    #create and configure the app
    app = Flask(__name__)
    configure_app(app)
    # get sqlalchemy object and create tables
    app.wsgi_app = ProxyFix(app.wsgi_app)
    db.init_app(app)
    with app.app_context():
        db.create_all() 

    #register routes and blueprints
    from backend.blueprints.load_bp import load_bp
    from backend.blueprints.twt_auth_bp import twt_auth_bp
    app.register_blueprint(twt_auth_bp)
    app.register_blueprint(load_bp)


    return app

FoO = create_app()
CORS(FoO, origins=[getenv('FRONTEND_URL')], methods=['GET', 'POST'], supports_credentials=True)
migrate = Migrate(FoO, db)

if __name__ == "__main__":
    FoO.run()