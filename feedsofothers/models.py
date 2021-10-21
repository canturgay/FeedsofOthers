from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime,  default=db.func.current_timestamp())
    last_sync = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_load = db.Column(db.JSON)