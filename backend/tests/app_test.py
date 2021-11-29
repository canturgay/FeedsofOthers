from os import getenv, environ

environ['FLASK_CONFIGURATION'] = 'testing'

from backend.app import app  
import pytest
from backend import models
from backend.db_helpers import db, base
from datetime import datetime

def test_secret():
    assert app.config['SECRET_KEY'] == getenv('SECRET_KEY')



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

@pytest.fixture
def db_session(connection):
    transaction = connection.begin()
    yield db.scoped_session(db.sessionmaker(autocommit=True, autoflush=True, bind=connection))
    transaction.rollback()

@pytest.fixture
def client(db_session):
    client = app.test_client()
    yield client

with app.test_client() as tester:

    def test_index():
        with tester.get("/", content_type="html/text") as response:
            assert response.status_code == 200, 304

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

    def test_register_user():
        with tester.post("/auth/register", json={
            "user_id": 12340000,
            "oauth_access_token": "NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0",
            "oauth_access_token_secret" : "veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI",
            "oauth_callback_confirmed": True
            }) as response:
            assert response.status_code == 201
            assert response.json == {'message': 'User registered'}

    def test_register_user_with_correct_data(db_session):
        session = db_session()
        assert session.query(models.User).first().id == 12340000
        assert session.query(models.User).first().oauth_token == 'NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0'
        assert session.query(models.User).first().oauth_token_secret == 'veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI'
        assert session.query(models.User).first().authenticated == True


    def test_register_user_already_exists():
        with tester.post("/auth/register", json={
            "user_id": 12340000,
            "oauth_access_token": "NPcudxy0yU5T3tBzho7iCotZ3cnetKwcTIRlX0iwRl0",
            "oauth_access_token_secret" : "veNRnAWe6inFuo8o2u8SLLZLjolYDmDP7SzL0YfYI",
            "oauth_callback_confirmed": True
            }) as response:
            assert response.status_code == 409
            assert response.json == {'message': 'User already exists'}
            


    