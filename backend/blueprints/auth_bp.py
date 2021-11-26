from flask import Blueprint, request, jsonify, redirect, url_for
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
    get_jwt_identity
)
from backend.models import User 

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    user_id = data['user_id']
    oauth_access_token = data['oauth_access_token'] 
    oauth_access_token_secret = data['oauth_access_token_secret']
    oauth_callback_confirmed = data['oauth_callback_confirmed']

    user = User.query.filter_by(id=user_id).first()
    try:
        if user is None:
            user = User(id=id, oauth_token=oauth_access_token, oauth_token_secret=oauth_access_token_secret, oauth_callback_confirmed=oauth_callback_confirmed)
            user.add()
            return 201
        else:
            return redirect(url_for('auth_bp.login', data=request.get_json()))
    except:
        return jsonify(message='An error occured'), 500

@auth_bp.route('/login', methods=['POST'])
def login(data):
    id = data['id']
    oauth_token = data['oauth_token']
    oauth_token_secret = data['oauth_token_secret']
    oauth_callback_confirmed = data['oauth_callback_confirmed']

    user = User.query.filter_by(id=id).first()

@auth_bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()
    access_token = create_access_token(identity=user.id)
    response = jsonify()
    set_access_cookies(response, access_token)
    return response, 201

