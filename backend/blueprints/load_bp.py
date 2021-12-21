from flask import Blueprint, request, jsonify
from backend.models import Tweet, Tag, tags
from backend.db_helpers import db

load_bp = Blueprint('load', __name__, url_prefix='/load')

@load_bp.route('/new', methods=['POST'])
def load_new():
    try:
        data = request.get_json()
        tags = data['tags']
        tweets = data['tweets']
    except:
        response = jsonify({'message': 'Error: missing data'})
        return response, 400

    return add_tweets(tweets, tags)
    

def add_tweets(tweets, tags):
    tweet_tags_dict = {}
    if len(tweets) > 0:
        for tw in tweets:
            if Tweet.query.filter_by(id=tw['id']).first() is not None:
                tweet = Tweet.query.filter_by(id=tw['id']).first()
            else:
                tweet = Tweet(
                id = tw['id'],
                created_at = tw['created_at'],
                content = tw['content'],
                hashtags = tw['hashtags'],
                user_id = tw['user_id'],
                user_name = tw['user_name'],
                tweet_url = tw['tweet_url'],
                contained_url = tw['contained_url'],
                quoted_id = tw['quoted_id'],
                quoted_user_id = tw['quoted_user_id'],
                quoted_user_name = tw['quoted_user_name'],
                quoted_content = tw['quoted_content'],
                quoted_url = tw['quoted_url'],
                quoted_status_contained_url = tw['quoted_status_contained_url'])
                language = tw['language']
            tweet_tags_dict[tweet] = []
        return add_tags(tags, tweet_tags_dict)
    else:
        response = jsonify({'message': 'Tweets couldnt be loaded'})
        return response, 400

def add_tags(tags, tweet_tags_dict):
    tags_list = []
    if len(tags) > 0:
        for tag in tags:
            if Tag.query.filter_by(name=tag).first() is not None:
                tag = Tag.query.filter_by(name=tag).first()
            else:
                tag = Tag(name=tag)
            tags_list.append(tag)
        return tweets_tags_merge(tags_list, tweet_tags_dict)
    else:
        response = jsonify({'message': 'Tags couldnt be loaded'})
        return response, 400

def tweets_tags_merge(tags_list, tweet_tags_dict):
    for tag in tags_list:
        for tweet in tweet_tags_dict:
            tag_list_as_value = tweet_tags_dict[tweet]
            tag_list_as_value.append(tag)
    return add_to_db(tweet_tags_dict)

def add_to_db(tweet_tags_dict):
    """add tags and tweets to the database"""
    for tweet in tweet_tags_dict:
        db.session.add(tweet)
        for tag in tweet_tags_dict[tweet]:
            db.session.add(tag)
    db.session.commit()
    response = jsonify({'message': 'Tweets and Tags added to the database'})
    return response, 201
