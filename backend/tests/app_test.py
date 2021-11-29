from os import getenv, environ

environ['FLASK_CONFIGURATION'] = 'testing'

from backend.app import create_app  
import pytest
from backend import models
from backend.db_helpers import base, db
from datetime import datetime

@pytest.fixture(scope="session")
def connection():
    engine = db.create_engine(getenv('TEST_DATABASE_URI'), {})
    return engine.connect()

@pytest.fixture(scope="session")
def setup_database(connection):
    base.metadata.bind = connection
    base.metadata.create_all()

    yield

    base.metadata.drop_all()

@pytest.fixture(scope="session")
def db_session(connection):
    transaction = connection.begin()
    yield db.scoped_session(db.sessionmaker(autocommit=True, autoflush=True, bind=connection))
    transaction.rollback()


@pytest.fixture(scope='session')
def tester():
    '''
    Create a Flask app context for the tests.
    '''
    FoO_test = create_app()
    tester = FoO_test.test_client()
    ctx = FoO_test.app_context()
    ctx.push()
    
    yield tester

    ctx.pop()


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
    new_user = models.User(id=12300000, oauth_token='NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0', oauth_token_secret='veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI', authenticated=True)
    session.add(new_user)
    last = session.query(models.User).first()
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

        


