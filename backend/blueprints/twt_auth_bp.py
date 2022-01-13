from flask import flash, redirect
from flask_login import current_user, login_user, login_required, logout_user
from flask_dance.contrib.twitter import make_twitter_blueprint
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound
from backend.models import User, OAuth
from os import getenv
from backend.helpers import db


twt_auth_bp = make_twitter_blueprint(
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
    api_key=getenv('TWITTER_CLIENT_KEY'),
    api_secret=getenv('TWITTER_CLIENT_SECRET'),
    authorized_url='/authorized',
)
@twt_auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@twt_auth_bp.route('/check')
def check():
    if not current_user.is_authenticated:
        return {}, 201
    #return current users user id
    return  db.session.query(OAuth).filter(OAuth.user_id == current_user.id).first().token, 200
    
# create/login local user on successful OAuth login
@oauth_authorized.connect_via(twt_auth_bp)
def twitter_logged_in(twt_auth_bp, token):
    if not token:
        flash("Failed to log in.", category="error")
        return False

    resp = twt_auth_bp.session.get("account/verify_credentials.json")
    if not resp.ok:
        msg = "Failed to fetch user info."
        flash(msg, category="error")
        return False

    info = resp.json()
    user_id = info["id_str"]
    

    # Find this OAuth token in the database, or create it
    query = db.session.query(OAuth).filter_by(
        provider=twt_auth_bp.name,
        user_id=user_id,
    )
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(
            provider=twt_auth_bp.name,
            user_id=user_id,
            token=token,
        )

    if oauth.user:
        login_user(oauth.user)
        flash("Successfully signed in.")

    else:
        # Create a new local user account for this user
        user = User(
            id=info["id"],
        )
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in.")

    # Disable Flask-Dance's default behavior for saving the OAuth token
    return False


# notify on OAuth provider error
@oauth_error.connect_via(twt_auth_bp)
def twitter_error(twt_auth_bp, message, response):
    msg = (
        "OAuth error from {name}! "
        "message={message} response={response}"
    ).format(
        name=twt_auth_bp.name,
        message=message,
        response=response,
    )
    flash(msg, category="error")

