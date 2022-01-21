from flask import Blueprint, request
from helpers import db
from flask_login import login_required
from models import Tweet, Tag, tagsTweets
from sqlalchemy.orm.exc import NoResultFound
import json

tweets_bp = Blueprint('tweets', __name__)


@tweets_bp.route('/', methods=['GET'])
@login_required
def get_tweets_by_tag():
    try:
        tag = request.args.get('lookup_tag')
        print(tag)
    except:
        raise Exception('Error! "lookup_tag" parameter is missing')

    try:
        tag_id = db.session.query(Tag.id).filter(Tag.name == tag).one()
        print(tag_id)
    except NoResultFound:
        raise Exception('Error! Tag not found')

    try:
        tweet_ids = db.session.query(tagsTweets).filter_by(tag_id=tag_id).all()
        print(tweet_ids)
    except NoResultFound:
        raise Exception("No tweets with this tag found")

    try:
        tweets = db.session.query(Tweet).filter(Tweet.id.in_(tweet_ids)).all()
        print(tweets)
    except NoResultFound:
        raise Exception("No tweets with this tag found")

    return json.dumps(tweets)


    
