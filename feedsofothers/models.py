from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    last_sync = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_load = db.Column(db.JSON)