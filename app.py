from flask import Flask, render_template
from os import getenv
from feedsofothers.models import db, User
from dotenv import load_dotenv



def configure_app(app):
    #configurations
    load_dotenv()
    configure = {
        "development": "config.devConfig",
        "production": "config.prodConfig",
    }

    #Determine the configuration file to read using environment variables
    config_name = getenv('FLASK_CONFIGURATION', 'development')
    
    #Read settings as objects
    app.config.from_object(configure[config_name])
    
    #Overwrite sensitive settings with the settings in the instance folder
    app.config.from_pyfile('config.cfg', silent=True)

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