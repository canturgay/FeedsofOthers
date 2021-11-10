from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = SQLAlchemy()

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TIMESTAMP,  default=db.func.current_timestamp())
    last_sync = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    last_load = db.Column(db.JSON)
    tags = relationship('Tag')

class Tag(base):
    __tablename__ = 'tag'
    tag = db.Column(db.String,  primary_key=True)
    tweet = relationship('Tweet', secondary='tag_tweet', backref='Tag')

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
    tags = relationship('Tag', secondary='tag_tweet', backref='Tweet')


