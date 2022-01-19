from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from flask_login import LoginManager



load_dotenv()

db = SQLAlchemy()
base = db.make_declarative_base(db.Model)
engine = db.create_engine(getenv('SQLALCHEMY_DATABASE_URI'), {})
metadata = db.metadata
login_manager = LoginManager()


