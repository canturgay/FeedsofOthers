from app import app 
from os import getenv
import config

with app.test_client() as tester:
    
    def test_index():
        with tester.get("/", content_type="html/text") as response:
            assert response.status_code == 200, 304

    def test_secret():  
        assert app.config['SECRET_KEY'] == getenv('SECRET_KEY')

    def test_config():
        if getenv('FLASK_CONFIGURATION') == 'development':
            assert app.config['TESTING'] 
        elif getenv('FLASK_CONFIGURATION') == 'production':
            assert app.config['TESTING'] == False
