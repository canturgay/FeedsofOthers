from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_migrate import Migrate
from sqlalchemy.engine import engine_from_config

db = SQLAlchemy()

class ENGINE_OPTIONS():
    'pool_size'= 10,
    'pool_recycle'= 120,
    'pool_pre_ping'= True,
    'echo'=True, 
    'echo_pool'=False,
    'pool_size'=10,
    'pool_recycle'=3600,
    'pool_timeout'=30,
    'pool_pre_ping'=True



base = db.make_declarative_base(db.Model)
metadata_obj = db.metadata
engine_config = { 'pool_size': 10, 'pool_recycle': 120, 'pool_pre_ping': True, 'echo': True, 'echo_pool': False, 'pool_size': 10, 'pool_recycle': 3600, 'pool_timeout': 30, 'pool_pre_ping': True}
engine = db.create_engine(getenv('DATABASE_URI'), engine_config)

