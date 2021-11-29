from flask import Blueprint, request, jsonify
from backend.models import Tweet, Tag, User
from backend.db_helpers import db

load_bp = Blueprint('load', __name__, url_prefix='/load')

@load_bp.route('/new', methods=['POST'])
def addtags():
    try:
        data = request.get_json()
        user_id = data['user_id']
        tags = [data['tags']]
        tweets = data['tweets']
        
        if User.query.filter_by(id=user_id).first() is not None:
            try:
                for tw in tweets:
                    try: 
                        tweet_id = tw['id']
                        if Tweet.query.filter_by(id=tweet_id).first() is not None:
                            tweet = Tweet.query.filter_by(id=tweet_id).first()
                            for tag in tags:
                                tweet.tags.append(tag)
                    except:
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
                        quoted_status_contained_url = tw['quoted_status_contained_url']
                        )
                        for tag in tags:
                            tweet.tags.append(tag)
                        db.session.add(tweet)
                db.session.commit()
                response = jsonify({'message': 'Successfully added tags and tweets'})
                return response, 201
            except:
                response = jsonify({'message': 'Tweets couldnt be loaded'})
                return response, 401
        else:
            response = jsonify({'message': 'Error: user not found'})
            return response, 400
    except:
        response = jsonify({'message': 'Error: missing data'})
        return response, 400
    


   
                
               






