from flask import Flask, render_template
from os import getenv
from models import db
from dotenv import load_dotenv

def configure_app(app):
    #configurations
    load_dotenv()
    configure = {
        "development": "config.devConfig",
        "production": "config.prodConfig",
        "staging": "config.stageConfig"
    }
    
    #Determine the configuration file to read using environment variables
    config_name = getenv('FLASK_CONFIGURATION', 'development')
    print(configure)
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

#routing
@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html', page_title='Feeds of Others')


if __name__ == "__main__":
    app.run()