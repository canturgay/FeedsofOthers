from re import S
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from flask_migrate import Migrate


load_dotenv()

db = SQLAlchemy()
base = db.make_declarative_base(db.Model)
engine = db.create_engine(getenv('DATABASE_URI'), {})    
metadata = db.metadata
migrate = Migrate(db=db, engine=engine)
session = db.session


