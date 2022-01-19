from helpers import db, base
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask_login import UserMixin


tagsTweets = db.Table('tagsTweets',
db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
db.Column('tweet_id', db.BigInteger, db.ForeignKey('tweet.id'), primary_key=True)
)

class User(base, UserMixin):
    __tablename__ = 'user'
    id = db.Column('id', db.BigInteger, primary_key=True)
    created_at = db.Column('created_at', db.TIMESTAMP,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.TIMESTAMP,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    tags = db.Column('tags', db.String)
    oauth = db.relationship('OAuth', uselist=False)

    def __repr__(self):
        return '<User %r>' % self.id

class OAuth(OAuthConsumerMixin, base):
    user_id = db.Column(db.BigInteger, db.ForeignKey(User.id))
    user = db.relationship(User, uselist=False)
    
class Tag(base):
    __tablename__ = 'tag'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    tweets = db.relationship('Tweet', secondary=tagsTweets, lazy='subquery') #Read think about lazy

    def __repr__(self):
        return '<Tag %r>' % self.id


class Tweet(base):
    __tablename__ = 'tweet'
    id = db.Column('id' ,db.BigInteger, primary_key=True)
    created_at = db.Column('created_at' ,db.String(100))
    content = db.Column('content', db.String(240))
    hashtags = db.Column('hashtags' ,db.String(240))
    user_id = db.Column('user_id' ,db.BigInteger)
    user_name = db.Column('user_name', db.String(30)) 
    tweet_url = db.Column('tweet_url', db.String(23))
    contained_url = db.Column('contained_url', db.String(100))
    quoted_id = db.Column('quoted_id', db.BigInteger, nullable=True)
    quoted_user_id = db.Column('quoted_user_id', db.BigInteger, nullable=True)
    quoted_hashtags = db.Column('quoted_hashtags', db.String(240))
    quoted_user_name = db.Column('quoted_user_name', db.String(30))
    quoted_url = db.Column('quoted_url', db.String(23))
    quoted_content = db.Column('quoted_content', db.String(240))
    quoted_status_contained_url = db.Column('quoted_status_contained_url', db.String(100))
    language = db.Column('lang', db.String(2), nullable=True)
    tags = db.relationship('Tag', secondary=tagsTweets, lazy='subquery') # Read about lazy

    def __repr__(self):
        return '<Tweet %r>' % self.id
   

