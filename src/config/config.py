import os
import sys
from ConfigParser import SafeConfigParser

path_to_config = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'config'))

def config(*args, **kwargs):
    parser = SafeConfigParser()
    parser.read(path_to_config)
    return parser.get(*args, **kwargs)
