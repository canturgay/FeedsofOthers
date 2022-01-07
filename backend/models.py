from backend.db_helpers import db, base
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin


tags = db.Table('tags',
db.Column('tag_name', db.String, db.ForeignKey('tag.name'), primary_key=True),
db.Column('tweet_id', db.BigInteger, db.ForeignKey('tweet.id'), primary_key=True)
)

class User(base):
    __tablename__ = 'user'
    id = db.Column('id', db.BigInteger, primary_key=True)
    oauth_token = db.Column('oauth_token', db.String)
    oauth_token_secret = db.Column('oauth_token_secret', db.String)
    created_at = db.Column('created_at', db.TIMESTAMP,  default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.TIMESTAMP,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    last_sync = db.Column('last_sync', db.TIMESTAMP, default=db.func.current_timestamp())
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.id

class OAuth(OAuthConsumerMixin, base):
    pass
   

class Tag(base):
    __tablename__ = 'tag'
    name = db.Column('name', db.String, primary_key=True)

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
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.id
   

