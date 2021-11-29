from flask import Flask, render_template
from os import getenv
from dotenv import load_dotenv
from flask_cors import CORS

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
    from backend.db_helpers import db
    db.init_app(app)
    with app.app_context():
        db.create_all() 

    #register routes and blueprints
    from backend.blueprints.auth_bp import auth_bp
    app.register_blueprint(auth_bp)

    @app.route("/", methods=['GET'])
    def hello_world():
        return render_template('index.html', page_title='Feeds of Others')

    return app

FoO = create_app()
CORS(FoO, origins=[getenv('FRONTEND_URL')], methods=['GET', 'POST'], supports_credentials=True)

if __name__ == "__main__":
    FoO.run()