from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv



load_dotenv()

db = SQLAlchemy()
base = db.make_declarative_base(db.Model)
engine = db.create_engine(getenv('SQLALCHEMY_DATABASE_URI'), {})    
metadata = db.metadata
session = db.session

