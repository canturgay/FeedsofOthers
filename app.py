from flask import Flask
import os
from feedsofothers.models import db, User
from dotenv import load_dotenv

def configure_app(app):
    #configurations
    config = {
        "development": "config.devConfig",
        "production": "config.prodConfig",
    }

    #Determine the configuration file to read using environment variables
    config_name = os.getenv('FLASK_CONFIGURATION')
    
    #Read settings as objects
    app.config.from_object(config[config_name])
    
    #Overwrite sensitive settings with the settings in the instance folder
    app.config.from_pyfile('config.cfg', silent=True)

load_dotenv()
app = Flask(__name__)
configure_app(app)
db.init_app(app)
with app.app_context():
        db.create_all()  # Create sql tables for our data models


#routing
@app.route("/", methods=['GET'])
def user_records():
    """Create a user"""
    new_user = User(
        last_load = {"key1": [1, 2, 3], "key2": [4, 5, 6]}
    )
    db.session.add(new_user)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return "successfully created!"


if __name__ == "__main__":
    app.run()