from flask import Flask, render_template
from os import getenv
from backend.models import db
from dotenv import load_dotenv
from flask_login import LoginManager



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
    app = Flask(__name__)
    configure_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()  
    return app

app = create_app()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.User.get(user_id)

#routing
@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html', page_title='Feeds of Others')





if __name__ == "__main__":
    app.run()