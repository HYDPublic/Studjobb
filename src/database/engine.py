import os
from sqlalchemy import create_engine
from src.config.config import config

if not os.environ.get('TEST'):
    host     = config.get("database", "host")
    user     = config.get("database", "user")
    password = config.get("database", "password")
    name     = config.get("database", "name")
    database = create_engine('mysql://%s:%s@%s/%s?charset=utf8' % (user, password, host, name))
else:
    database = None
