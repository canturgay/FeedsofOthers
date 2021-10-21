from flask import Flask
import os
from feedsofothers.models import db


def configure_app(app):
    #configurations
    config = {
        "development": "config.devConfig",
        "testing": "config.testConfig",
    }

    #Determine the configuration file to read using environment variables
    config_name = os.getenv('FLASK_CONFIGURATION', 'development')
    
    #Read settings as objects
    app.config.from_object(config[config_name])
    
    #Overwrite sensitive settings with the settings in the instance folder
    app.config.from_pyfile('config.cfg', silent=True)

app = Flask(__name__)
configure_app(app)
db.init_app(app)

#routing
@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()