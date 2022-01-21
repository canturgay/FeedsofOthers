from flask import Flask, render_template
import requests
from os import getenv, path
from dotenv import load_dotenv
from helpers import db, login_manager
from models import User
from flask_session import Session
from flask_caching import Cache

def configure_app(app):
    #configurations
    load_dotenv()
    configure = {
        "development": "config.devConfig",
        "production": "config.prodConfig",
        "staging": "config.stageConfig",
        "testing": "config.testConfig"
    }
    
    #Determine the configuration file to read using environment variables
    config_name = getenv('FLASK_CONFIGURATION', 'development')
    #Read settings as objects
    app.config.from_object(configure[config_name])
    return app.config

def create_app():
    #get the absolute path of the parent directory
    dist_dir = path.abspath('./dist')
    static_dir = path.join(dist_dir, 'static')
    #create and configure the app
    app = Flask(__name__, static_folder=static_dir, template_folder=dist_dir)
    configure_app(app)
    #app.wsgi_app = ProxyFix(app.wsgi_app) // I dont remember why I did this hence commented out
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager.init_app(app) 
    server_session = Session(app)
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    #register routes and blueprints
    from api.load_api import load_bp
    from api.twt_auth_api import twt_auth_bp
    from api.tweets_api import tweets_bp 
    from api.tags_api import tags_bp

    app.register_blueprint(twt_auth_bp, url_prefix='/auth')
    app.register_blueprint(tweets_bp, url_prefix='/tweets')
    app.register_blueprint(tags_bp, url_prefix='/tags')
   
    @login_manager.user_loader
    def load_user(user_id):
        user = db.session.query(User).get(user_id)
        if user:
            return user 
        else:
            return None
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        if getenv('FLASK_CONFIGURATION') != 'production':
            return requests.get('http://localhost:8080/{}'.format(path)).text

        return render_template("index.html")

    return app

FoO = create_app()

if __name__ == "__main__":
    FoO.run()