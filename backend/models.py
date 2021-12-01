from backend.db_helpers import db, base


tags = db.Table('tags',
db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
db.Column('tweet_id', db.Integer, db.ForeignKey('tweet.id'), primary_key=True)
)

class User(base):
    __tablename__ = 'user'
    id = db.Column('id', db.Integer, primary_key=True)
    oauth_token = db.Column('oauth_token', db.String(100))
    oauth_token_secret = db.Column('oauth_token_secret', db.String(100))
    created_at = db.Column('created_at', db.TIMESTAMP,  default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.TIMESTAMP,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    last_sync = db.Column('last_sync', db.TIMESTAMP, default=db.func.current_timestamp())
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.id
   
    

class Tag(base):
    __tablename__ = 'tag'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String, unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.id



class Tweet(base):
    __tablename__ = 'tweet'
    id = db.Column('id' ,db.Integer, primary_key=True)
    created_at = db.Column('created_at' ,db.DateTime)
    content = db.Column('content', db.String(240))
    hashtags = db.Column('hashtags' ,db.String(240))
    user_id = db.Column('user_id' ,db.Integer)
    user_name = db.Column('user_name', db.String(15)) 
    tweet_url = db.Column('tweet_url', db.String(23))
    contained_url = db.Column('contained_url', db.String(100))
    quoted_id = db.Column('quoted_id', db.Integer, nullable=True)
    quoted_user_id = db.Column('quoted_user_id', db.Integer, nullable=True)
    quoted_hashtags = db.Column('quoted_hashtags', db.String(240))
    quoted_user_name = db.Column('quoted_user_name', db.String(15))
    quoted_url = db.Column('quoted_url', db.String(23))
    quoted_content = db.Column('quoted_content', db.String(240))
    quoted_status_contained_url = db.Column('quoted_status_contained_url', db.String(100))
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.id
   

