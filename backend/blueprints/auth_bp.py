from flask import Blueprint, request, jsonify, redirect, url_for
from backend.models import User 
from backend.db_helpers import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user_id = data['user_id']
        oauth_access_token = data['oauth_access_token'] 
        oauth_access_token_secret = data['oauth_access_token_secret']
        oauth_callback_confirmed = data['oauth_callback_confirmed']
    except:
        response = jsonify({'message': 'Error: missing data'})
        return response, 400

    try:
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            user = User(id=user_id, oauth_token=oauth_access_token, oauth_token_secret=oauth_access_token_secret, authenticated=oauth_callback_confirmed)
            db.session.add(user)
            db.session.commit()
            response = jsonify({'message': 'User registered'})
            return response, 201
        else:
            response = jsonify({'message': 'User already exists'})
            return response , 409
    except:
        return jsonify(message='An error occured'), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user_id = data['user_id']
        oauth_access_token = data['oauth_access_token'] 
        oauth_access_token_secret = data['oauth_access_token_secret']
    except:
        return jsonify(message='An error occured'), 500





