from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer(11), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_sync = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_load = db.Colum(db.JSON)