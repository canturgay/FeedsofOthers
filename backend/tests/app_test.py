from backend import models
from backend.db_helpers import db
from datetime import datetime
"""
def test_index(tester):
    with tester.get("/register", content_type="html/text") as response:
        assert response.status_code == 302

def test_db_tables_exists():
    assert db.inspect(models.User) is not None
    assert db.inspect(models.Tag) is not None
    assert db.inspect(models.Tweet) is not None
    assert db.inspect(models.tags) is not None

def test_declarative_class_matches_db_table():
    assert models.User.__table__ == db.inspect(models.User).local_table
    assert models.Tag.__table__ == db.inspect(models.Tag).local_table
    assert models.Tweet.__table__ == db.inspect(models.Tweet).local_table

def test_db_add_user(db_session):
    session = db_session()
    new_user = models.User(id=123500000, token={cnetKwcTIRlX0iwRl0'}, authenticated=True)
    session.add(new_user)
    last = session.query(models.User).order_by(models.User.created_at.desc()).first()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_created_at = last.created_at.strftime("%Y-%m-%d %H:%M:%S")
    assert last == new_user
    assert now == last_created_at
    session.delete(new_user)

def test_save_add_tags_and_tweets(tester):
    with tester.post("/load/new", json={
        "user_id": 12340000,
        "tags": ["test", "test2", "test3"],
        "tweets": [{
            'id': 1464209084735963137,
            'created_at': "Fri Nov 26 12:27:04 +0000 2021",
            'content': "test tweet",
            'hashtags': ["#hash", "#tag"],
            'user_id': 99620272,
            'user_name': 'twitter_test_user',
            'tweet_url': 'https://t.co/28WMHvRfS0',
            'contained_url': 'https://t.co/28WMHvRfG0',
            'quoted_id': 99620272,
            'quoted_user_id': 99620272,
            'quoted_hashtags': [],
            'quoted_user_name': [],
            'quoted_url': [],
            'quoted_content': [],
            'quoted_status_contained_url': [],
            'language': 'en'
        }, {
            'id': 1464209084735963138,
            'created_at': "Fri Nov 26 12:27:04 +0000 2021",
            'content': "test tweet",
            'hashtags': ["#hash", "#tag"],
            'user_id': 99620272,
            'user_name': 'twitter_test_user',
            'tweet_url': 'https://t.co/28WMHvRfS0',
            'contained_url': 'https://t.co/28WMHvRfG0',
            'quoted_id': 99620272,
            'quoted_user_id': 99620272,
            'quoted_hashtags': [],
            'quoted_user_name': [],
            'quoted_url': [],
            'quoted_content': [],
            'quoted_status_contained_url': [],
            'language': "null"
        }]
        }) as response:
        assert response.status_code == 201
        assert response.json == {'message': 'Tweets and Tags added to the database'}

def test_add_tags_and_tweets_missing_data(tester):
    with tester.post("/load/new", json={
        "user_id": 12340000,
    }) as response:
        assert response.status_code == 400
        assert response.json == {'message': 'Error: missing data'}


def test_add_tags_and_tweets_no_tweets(tester):
    with tester.post("/load/new", json={
        "user_id": 12340000,
        "tags": ["test", "test2", "test3"],
        "tweets": []
        }) as response:
        assert response.status_code == 400
        assert response.json == {'message': 'Tweets couldnt be loaded'}

def test_add_tags_and_tweets_no_tags(tester):
    with tester.post("/load/new", json={
        "user_id": 12340000,
        "tags": [],
        "tweets": [{
            'id': 1464209084735963137,
            'created_at': "Fri Nov 26 12:27:04 +0000 2021",
            'content': "test tweet",
            'hashtags': ["#hash", "#tag"],
            'user_id': 99620272,
            'user_name': 'twitter_test_user',
            'tweet_url': 'https://t.co/28WMHvRfS0',
            'contained_url': 'https://t.co/28WMHvRfG0',
            'quoted_id': 99620272,
            'quoted_user_id': 99620272,
            'quoted_hashtags': [],
            'quoted_user_name': [],
            'quoted_url': [],
            'quoted_content': [],
            'quoted_status_contained_url': []
        }]
        }) as response:
        assert response.status_code == 400
        assert response.json == {'message': 'Tags couldnt be loaded'}
"""