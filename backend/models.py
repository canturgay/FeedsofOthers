from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP,  default=db.func.current_timestamp())
    last_sync = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    last_load = db.Column(db.JSON)

class Tag(base):
    __tablename__ = 'tag'
    tag_id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String,  default=db.func.current_timestamp())