import os
from sqlalchemy   import create_engine
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read(os.path.abspath(os.path.join(__file__, '..', '..', '..', 'config')))

host     = config.get("database", "host")
user     = config.get("database", "user")
password = config.get("database", "password")
name     = config.get("database", "name")

database = create_engine('mysql://%s:%s@%s/%s?charset=utf8' % (user, password, host, name))
