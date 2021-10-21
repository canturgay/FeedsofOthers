from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# env var set
load_dotenv(finddotenv())

# initialize sql-alchemy
db = SQLAlchemy()

# create and initialize a new Flask app
app = Flask(__name__)

#configurations
config = {
    "development": "bookshelf.config.devConfig",
    "testing": "bookshelf.config.testConfig",
}

def configure_app(app):
    #Determine the configuration file to read using environment variables
    config_name = os.getenv('FLASK_CONFIGURATION', 'development')
    
    #Read settings as objects
    app.config.from_object(config[config_name])
    
    #Overwrite sensitive settings with the settings in the instance folder
    app.config.from_pyfile('config.cfg', silent=True)


#routing
@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()