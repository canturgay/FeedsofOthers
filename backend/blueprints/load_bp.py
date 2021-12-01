from flask import Blueprint, request, jsonify
from backend.models import Tweet, Tag, User
from backend.db_helpers import db

load_bp = Blueprint('load', __name__, url_prefix='/load')

@load_bp.route('/new', methods=['POST'])

def tweets(tweets):
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
            tweet_tags_dict[tweet] = None
        return tweet_tags_dict
    else:
        response = jsonify({'message': 'Tweets couldnt be loaded'})
        return response
        
            




def addtags():
    try:
        data = request.get_json()
        user_id = data['user_id']
        tags = data['tags']
        tweets = data['tweets']
        if User.query.filter_by(id=user_id).first() is not None:
            if len(tweets) > 0:
                for tw in tweets:
                    if Tweet.query.filter_by(id=tw['id']).first() is not None:
                        tweet = Tweet.query.filter_by(id=tw['id']).first()
                        if len(tags) > 0:
                            for tag in tags:
                                new_tag = Tag(name=tag)
                                tweet.tags.append(new_tag)
                            db.session.add(tweet)
                            db.session.commit()
                            response = jsonify({'message': 'Successfully added tags and tweets'})
                            return response, 201 
                        else:
                            response = jsonify({'message': 'No tags were provided'})
                            return response, 400
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
                        quoted_status_contained_url = tw['quoted_status_contained_url']
                        )
                        if len(tags) > 0:
                            for tag in tags:
                                new_tag = Tag(name=tag)
                                tweet.tags.append(new_tag)
                            db.session.add(tweet)
                            db.session.commit()
                            response = jsonify({'message': 'Successfully added tags and tweets'})
                            return response, 201
                        else:
                            response = jsonify({'message': 'No tags were provided'})
                            return response, 400
            else:
                response = jsonify({'message': 'Tweets couldnt be loaded'})
                return response, 400
        else:
            response = jsonify({'message': 'Error: user not found'})
            return response, 400
    except Exception as e:
        response = jsonify({'Error': f'{e}'})
        print(f'{e}')
        return response, 400
    


   
                
               






