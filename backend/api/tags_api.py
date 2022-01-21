from flask import Blueprint, request
from helpers import db
from flask_login import login_required, current_user
from models import User
from api.twt_auth_api import twt_auth_bp
import json

tags_bp = Blueprint('tags', __name__)


@tags_bp.route('/', methods=['POST'])
@login_required
def share_tags_tweets():
    try:
        self_tags = request.args.getlist('self_tags')
    except Exception as e:
        raise Exception(f'Error! {e} ')

    try:
        if db.session.query(User).filter(id == current_user.id).first() != None:
            for tags in db.session.query(User).filter(id == current_user.id).first().tags:
                for tag in tags:
                    if tag in self_tags:
                        print('tag already in user tags')
                        self_tags.remove(tag)
    except Exception as e:
        raise Exception(f'Error! {e} ')
    
    db.session.query(User).filter(id==current_user.id).update({'tags': self_tags})
    db.session.commit()


    twt_load = twt_auth_bp.session.get('/1.1/statuses/home_timeline.json').json()

    return json.dumps(twt_load)







        





    
