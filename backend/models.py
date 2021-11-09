from typing import Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP,  default=db.func.current_timestamp())
    last_sync = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    last_load = db.Column(db.JSON)

class Tag(base):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String,  default=db.func.current_timestamp())

class Tweet(base):
    __tablename__ = 'resource'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    content = db.Column(db.String(240))
    hashtags = db.Column(db.String(240))
    user_id = db.Column(db.Integer)
    user_name = db.Column(db.String(15)) 
    tweet_url = db.Column(db.String(23))
    contained_url = db.Column(db.String(100))
    quoted_id = db.Column(db.Integer)
    quoted_user_id = db.Column(db.Integer)
    quoted_hashtags = db.Column(db.String(240))
    quoted_user_name = db.Column(db.String(15))
    quoted_url = db.Column(db.String(23))
    quoted_content = db.Column(db.String(240))
    quoted_status_contained_url = db.Column(db.String(100))

class User_Tag(base):
    __tablename__ = 'user_tag'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    tag_id = db.Column(db.Integer)

class Tag_Tweet(base):
    __tablename__ = 'tag_tweet'
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer)
    tweet_id = db.Column(db.Integer)
