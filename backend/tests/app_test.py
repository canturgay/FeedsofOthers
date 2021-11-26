from os import getenv, environ

environ['FLASK_CONFIGURATION'] = 'testing'

from backend.app import app  
import pytest
from backend import models
from backend.db_helpers import db, base
from datetime import datetime

def test_env_conf():
        if getenv('FLASK_CONFIGURATION') == 'development':
            assert getenv('FLASK_ENV') == 'development', app.config['TESTING']
            assert app.config['DEBUG']
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('DATABASE_URI')
        elif getenv('FLASK_CONFIGURATION') == 'testing':
            assert app.config['TESTING']
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('TEST_DATABASE_URI')
        else:
            raise ValueError('unexpected FLASK_CONFIGURATION')

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

    

with app.test_client() as tester:

    session = db_session
    
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

    def test_db_add_user(session):
        new_user = models.User(last_load = {"key1": [2, 3, 1], "key2": [4, 5, 6]})
        session.add(new_user)
        last = session.query(models.User).first()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_created_at = session.query(models.User).with_entities(models.User.created_at).scalar().strftime("%Y-%m-%d %H:%M:%S")
        assert last == new_user
        assert now == last_created_at
            


    