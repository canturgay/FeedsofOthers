from os import getenv, environ

environ['FLASK_CONFIGURATION'] = 'testing'

from backend.app import create_app  
import pytest
from backend import models
from backend.db_helpers import db, base
from datetime import datetime
from sqlalchemy.orm import Session

@pytest.fixture(scope="session")
def app():
    #Returns session-wide application.
    FoO_test = create_app()
    yield FoO_test
    with FoO_test.app_context():
        db.drop_all()

@pytest.fixture(scope='session')
def tester(app):
    #Create a Flask app context for the tests.
    with app.app_context():
        tester = app.test_client()
        yield tester

@pytest.fixture(scope="session")
def engine(app):
    #create db engine, yield and drop
    with app.app_context():
        engine = db.engine.connect()
        yield engine
        engine.close()


@pytest.fixture(scope="session")
def db_session(engine):
    #Create a session for the tests and rollback at the end.
    transaction = engine.begin()
    session = db.scoped_session(db.sessionmaker(autocommit=True, autoflush=True, bind=engine))
    yield session
    session.close()
    transaction.rollback()

def test_index(tester):
    with tester.get("/", content_type="html/text") as response:
        assert response.status_code == 200

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
    new_user = models.User(id=123500000, oauth_token='NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0', oauth_token_secret='veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI', authenticated=True)
    session.add(new_user)
    last = session.query(models.User).order_by(models.User.created_at.desc()).first()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_created_at = last.created_at.strftime("%Y-%m-%d %H:%M:%S")
    assert last == new_user
    assert now == last_created_at
    session.delete(new_user)

def test_register_user(tester):
    with tester.post("/auth/register", json={
        "user_id": 12340000,
        "oauth_access_token": "NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0",
        "oauth_access_token_secret" : "veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI",
        "oauth_callback_confirmed": True
        }) as response:
        assert response.status_code == 201
        assert response.json == {'message': 'User registered'}


def test_register_user_already_exists(tester):
    with tester.post("/auth/register", json={
        "user_id": 12340000,
        "oauth_access_token": "NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0",
        "oauth_access_token_secret" : "veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI",
        "oauth_callback_confirmed": True
        }) as response:
        assert response.status_code == 409
        assert response.json == {'message': 'User already exists'}

def test_registered_user_data(db_session):
    assert db_session.query(models.User).first().id == 12340000
    assert db_session.query(models.User).first().oauth_token == 'NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0'
    assert db_session.query(models.User).first().oauth_token_secret == 'veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI'
    assert db_session.query(models.User).first().authenticated == True
        


