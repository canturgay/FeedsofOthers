from app import app, db 
from os import getenv
import config

with app.test_client() as tester:
    
    def test_index():
        with tester.get("/", content_type="html/text") as response:
            assert response.status_code == 200, 304

    def test_db():
        pass

    def test_secret():
        assert app.config['SECRET_KEY'] == getenv('SECRET_KEY')

    def test_config():
        if getenv('FLASK_CONFIGURATION') == 'development':
            assert app.config['TESTING']
            assert app.config['DEBUG']
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('TEST_DATABASE_URI')
        elif getenv('FLASK_CONFIGURATION') == 'production':
            assert not app.config['TESTING']
            assert not app.config['DEBUG'] 
            assert app.config['SQLALCHEMY_DATABASE_URI'] == getenv('DATABASE_URI')
        else:
            raise ValueError('unexpected FLASK_CONFIGURATION')