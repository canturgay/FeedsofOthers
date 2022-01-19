from flask import Blueprint, request
from helpers import db
from flask_login import login_required
from models import Tweet, Tag, tagsTweets
from sqlalchemy.orm.exc import NoResultFound

get_bp = Blueprint('get', __name__, url_prefix='/get')


@get_bp.route('/')
@login_required
def get_tweets_by_tag():
    try:
        tag = request.args.get('lookup_tag')
    except:
        raise Exception('Error! "lookup_tag" parameter is missing')

    try:
        tag_id = db.session.query(Tag.id).filter(Tag.name == tag).one()
    except NoResultFound:
        raise Exception('Error! Tag not found')

    try:
        tweet_ids = db.session.query(tagsTweets).filter_by(tag_id=tag_id).all()
    except NoResultFound:
        raise Exception("No tweets with this tag found")

    try:
        tweets = db.session.query(Tweet).filter(Tweet.id.in_(tweet_ids)).all()
    except NoResultFound:
        raise Exception("No tweets with this tag found")

    return tweets

    
