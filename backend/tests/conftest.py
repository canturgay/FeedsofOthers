from os import getenv, environ
from backend.app import create_app  
import pytest
from backend.db_helpers import db

environ['FLASK_CONFIGURATION'] = 'testing'

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