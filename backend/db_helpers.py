from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from marshmallow import Schema, fields



load_dotenv()

db = SQLAlchemy()
base = db.make_declarative_base(db.Model)
engine = db.create_engine(getenv('SQLALCHEMY_DATABASE_URI'), {})    
metadata = db.metadata

class UserSchema(Schema):
    id = fields.Int()
    provider = fields.Str()
    created_at = fields.DateTime()
    token = fields.Str()
    updated_at = fields.DateTime()
    last_sync = fields.DateTime()
    oauth_token = fields.Str()
    oauth_token_secret = fields.Str()
    
