from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
app = Flask(__name__, template_folder = 'views', static_folder = 'assets')
