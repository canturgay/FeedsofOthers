from flask import Blueprint, request, jsonify, redirect, url_for
from backend.models import User 
from backend.db_helpers import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_id = data['user_id']
    oauth_access_token = data['oauth_access_token'] 
    oauth_access_token_secret = data['oauth_access_token_secret']
    oauth_callback_confirmed = data['oauth_callback_confirmed']

    
    try:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            user = User(id=user_id, oauth_token=oauth_access_token, oauth_token_secret=oauth_access_token_secret, authenticated=oauth_callback_confirmed)
            db.session.add(user)
            #access_token = create_access_token(identity=user.id)
            #refresh_token = create_refresh_token(identity=user.id)
            
            response = jsonify({'message': 'User registered'})
            #set_access_cookies(response, access_token)
            #set_refresh_cookies(response, refresh_token)

            return response, 201
        else:
            return redirect(url_for('auth_bp.login', data=request.get_json()))
    except:
        return jsonify(message='An error occured'), 500





