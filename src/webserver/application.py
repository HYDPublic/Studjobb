from flask import Flask
app = Flask(__name__, template_folder = 'views', static_folder = 'assets')
