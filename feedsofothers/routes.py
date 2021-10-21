from flask import current_app, Blueprint, render_template
feed = Blueprint('feed', __name__)


@feed.route("/", methods=['GET'])
def user_records():
    """Create a user"""
    new_user = User(last_load = {"key1": [1, 2, 3], "key2": [4, 5, 6]})
    db.session.add(new_user)  
    db.session.commit()  
    users=User.query.all()
    return render_template('index.html', page_title='Feeds of Others')