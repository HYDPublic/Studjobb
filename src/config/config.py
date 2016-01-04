import os
from os.path import abspath, join
from ConfigParser import SafeConfigParser

class Config(object):

    def __init__(self, location):
        self.parser = SafeConfigParser()
        self.parser.read(location)

    def get(self, *args, **kwargs):
        return self.parser.get(*args, **kwargs)

if os.environ.get('TEST'):
    config_file_name = 'example_config'
else:
    config_file_name = 'config'

location = abspath(join(__file__, '..', '..', '..', config_file_name))
print location
config = Config(location)
