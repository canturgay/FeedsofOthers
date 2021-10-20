from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, finddotenv

# env var set
load_dotenv(finddotenv())


# initialize sql-alchemy
db = SQLAlchemy()

# create and initialize a new Flask app
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()