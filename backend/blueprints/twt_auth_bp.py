from flask_dance.consumer import OAuth1ConsumerBlueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.contrib.twitter import twitter
from functools import partial
from flask.globals import LocalProxy, _lookup_app_object
from os import getenv
from backend.db_helpers import db, UserSchema
from backend.models import User, OAuth
from flask import _app_ctx_stack as stack, redirect, url_for



twt_auth_bp = OAuth1ConsumerBlueprint(
    "twt_auth_bp",
    __name__,
    client_key=getenv("TWITTER_CLIENT_KEY"),
    client_secret=getenv("TWITTER_CLIENT_SECRET"),
    base_url="https://api.twitter.com/1.1/",
    request_token_url="https://api.twitter.com/oauth/request_token",
    access_token_url="https://api.twitter.com/oauth/access_token",
    authorization_url="https://api.twitter.com/oauth/authorize",
    redirect_url=None,
    redirect_to=None,
    login_url=None,
    authorized_url=None,
    session_class=None,
    storage=SQLAlchemyStorage(OAuth, db.session),
    rule_kwargs=None,
    url_prefix='/auth'
    )

@twt_auth_bp.before_app_request
def set_applocal_session():
    ctx = stack.top
    ctx.twitter_oauth = twt_auth_bp.session


@twt_auth_bp.route('/')
def index():
        if not twitter.authorized:
            return redirect(url_for('twt_auth_bp.login'))
        token = twitter.token
        if db.session.query(User).filter_by(id=token['user_id']).first() is None:
            user = User(id=token['token'], oauth_token=token['oauth_token'], oauth_token_secret=token['oauth_token_secret'])
            db.session.add(user)
            db.session.commit()
            return "User added, "
        else:
            user = db.session.query(User).filter_by(id=token['user_id']).first()
            user.oauth_token = token['oauth_token']
            user.oauth_token_secret = token['oauth_token_secret']
            db.session.commit()
            return f"User already exists, token is {token['oauth_token']}"



@twt_auth_bp.route('/check')
def check():
    last = db.session.query(User).order_by(User.created_at.desc()).first()
    schema = UserSchema()
    user = schema.dump(last)
    return user

twitter = LocalProxy(partial(_lookup_app_object, "twitter_oauth"))