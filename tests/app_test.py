from app import app 
import flask_sqlalchemy 
import pytest
from os import getenv
from feedsofothers import models
from feedsofothers.models import db , User

@pytest.fixture(scope="session")
def connection():
    engine = models.db.create_engine(getenv('TEST_DATABASE_URI'), {})
    return engine.connect()

@pytest.fixture(scope="session")
def setup_database(connection):
    models.Base.metadata.bind = connection
    models.Base.metadata.create_all()

    yield

    models.Base.metadata.drop_all()

@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield models.db.scoped_session(models.db.sessionmaker(autocommit=False, autoflush=False, bind=connection))
    transaction.rollback()

with app.test_client() as tester:
    
    def test_index():
        with tester.get("/", content_type="html/text") as response:
            assert response.status_code == 200, 304

    def test_db_add_user(db_session):
        new_user = User(last_load = {"key1": [1, 2, 3], "key2": [4, 5, 6]})
        db_session.add(new_user)
        db_session.commit
        last = db_session.query(User).all()
        assert last.pop() == new_user

    

    def test_secret():
        assert app.config['SECRET_KEY'] == getenv('SECRET_KEY')

    def test_env_conf():
        if getenv('FLASK_CONFIGURATION') == 'development':
            assert getenv('FLASK_ENV') == 'development', app.config['TESTING']
            assert app.config['DEBUG']
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('TEST_DATABASE_URI')
        elif getenv('FLASK_CONFIGURATION') == 'production':
            assert getenv('FLASK_ENV') == 'production'
            assert not app.config['TESTING']
            assert not app.config['DEBUG'] 
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('DATABASE_URI')
        else:
            raise ValueError('unexpected FLASK_CONFIGURATION')

