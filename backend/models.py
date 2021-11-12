from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship

db = SQLAlchemy()
base = db.make_declarative_base(db.Model)
metadata_obj = db.metadata


class User(base):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    created_at = db.Column('created_at', db.TIMESTAMP,  default=db.func.current_timestamp())
    last_sync = db.Column('last_sync', db.TIMESTAMP, default=db.func.current_timestamp())
    last_load = db.Column('last_load', db.JSON)

    def __repr__(self):
        return '<User %r>' % self.id
   
    

class Tag(base):
    __tablename__ = 'tag'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String, unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.id



class Tweet(base):
    __tablename__ = 'resource'
    id = db.Column('id' ,db.Integer, primary_key=True)
    created_at = db.Column('created_at' ,db.DateTime)
    content = db.Column('content', db.String(240))
    hashtags = db.Column('hashtags' ,db.String(240))
    user_id = db.Column('user_id' ,db.Integer)
    user_name = db.Column('user_name', db.String(15)) 
    tweet_url = db.Column('tweet_url', db.String(23))
    contained_url = db.Column('contained_url', db.String(100))
    quoted_id = db.Column('quoted_id', db.Integer)
    quoted_user_id = db.Column('quoted_user_id', db.Integer)
    quoted_hashtags = db.Column('quoted_hashtags', db.String(240))
    quoted_user_name = db.Column('quoted_user_name', db.String(15))
    quoted_url = db.Column('quoted_url', db.String(23))
    quoted_content = db.Column('quoted_content', db.String(240))
    quoted_status_contained_url = db.Column('quoted_status_contained_url', db.String(100))

    def __repr__(self):
        return '<Tweet %r>' % self.id
   

class Tag_Tweet(base):
    __tablename__ = 'tag_tweet'
    id = db.Column('id', db.Integer, primary_key=True)
    tag = db.Column('tag', db.String, db.ForeignKey('tag.name'))
    tweet = db.Column('tweet', db.Integer, db.ForeignKey('resource.id'))

