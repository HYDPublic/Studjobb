# -*- coding: utf-8 -*-
import sys
import os
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from flask import Flask
from flask import render_template
from flask import abort 
from flask import request
from flask import redirect 
from flask import send_from_directory
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(
    __name__,
    template_folder = 'views',
    static_folder   = 'assets'
)

if __name__ == '__main__':
    app.run(debug = True)
