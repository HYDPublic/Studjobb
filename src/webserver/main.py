# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from urls import app

if __name__ == '__main__':
    app.run(debug = True)
