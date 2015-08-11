# -*- coding: utf-8 -*-
import sys
import os
# Needs fixing:
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), os.pardir))

from flask import Flask
from flask import render_template
from flask import request

from src.database.engine import database
from src.database.job_repository import JobRepository
from src.database.board_repository import BoardRepository
    
# Configuration
app = Flask(__name__, template_folder = 'views', static_folder = 'assets')

# Repositories
job_repository = JobRepository(database)
board_repository = BoardRepository(database)

# Routes
@app.route('/')
def board():
    board = board_repository.find()
    board.filterExpiredJobs()
    return render_template('board.html', jobs = board.jobs) 

@app.route('/stilling/<int:id>')
def job(id):
    job = job_repository.find(id)
    return render_template('job.html', job = job) 

@app.route('/innlogging', methods = ['GET'])
def login():
    return render_template('login.html') 

@app.route('/innlogging', methods = ['POST'])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    print email, password
    return render_template('login.html') 

@app.route('/om')
def about():
    return render_template('about.html') 

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return query

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
