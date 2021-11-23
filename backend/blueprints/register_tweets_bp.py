from flask import Blueprint, request, jsonify
from backend.models import Tweet

register_tweets = Blueprint('tweet_parse_bp', __name__)

@register_tweets.route('/tweets', methods=['post'])
def register_tweets():
    data = request.get_json()
    tweets = data['tweets']
    tags = data['tags']

