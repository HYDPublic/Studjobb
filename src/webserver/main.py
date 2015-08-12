# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect 
from flask.ext.httpauth import HTTPBasicAuth

from src.database.engine import database
from src.database.job_repository import JobRepository
from src.database.user_repository import UserRepository
from src.database.board_repository import BoardRepository
from src.database.company_repository import CompanyRepository

from src.company.company import Company
    
# Configuration
app  = Flask(__name__, template_folder = 'views', static_folder = 'assets')
auth = HTTPBasicAuth()

# Repositories
job_repository = JobRepository(database)
user_repository = UserRepository(database)
board_repository = BoardRepository(database)
company_repository = CompanyRepository(database)

# Authentication
@auth.verify_password
def verify_pw(email, password):
    user = user_repository.find(email)
    if user is None:
        return False
    return user.checkCredentials(password)

# Routes
@app.route('/admin')
@auth.login_required
def admin():
    board = board_repository.find()
    board.filterExpiredJobs()
    return render_template('admin/admin.html', jobs = board.jobs)

@auth.login_required
@app.route('/admin/stilling/<int:id>', methods = ['GET'])
def edit_job(id):
    job = job_repository.find(id)
    return render_template('admin/job/edit.html', job = job) 

@auth.login_required
@app.route('/admin/stilling/<int:id>', methods = ['POST'])
def save_job(id):
    job = job_repository.find(id)
    job.title = request.form['title']
    job.description = request.form['description']
    job = job_repository.save(job) 
    return render_template('admin/job/edit.html', job = job) 

@auth.login_required
@app.route('/admin/selskap/<int:id>', methods = ['GET'])
def edit_company(id):
    company = company_repository.find(id)
    return render_template('admin/company/edit.html', company = company) 

@auth.login_required
@app.route('/admin/selskap/<int:id>', methods = ['POST'])
def save_company(id):
    company = company_repository.find(id)
    company.name = request.form['name']
    company.logo = request.form['logo'].encode('utf8')
    company = company_repository.save(company) 
    return render_template('admin/company/edit.html', company = company) 

@auth.login_required
@app.route('/admin/selskap', methods = ['GET'])
def new_company():
    return render_template('admin/company/new.html') 

@auth.login_required
@app.route('/admin/selskap', methods = ['POST'])
def create_company():
    company = Company() 
    company.name = request.form['name']
    company.logo = request.form['logo'].encode('utf8')
    company = company_repository.save(company) 
    return redirect('/admin/selskap/%d' % company.id)

@app.route('/')
def board():
    board = board_repository.find()
    board.filterExpiredJobs()
    return render_template('public/index.html', jobs = board.jobs) 

@app.route('/stilling/<int:id>')
def job(id):
    job = job_repository.find(id)
    return render_template('public/job.html', job = job) 

@app.route('/om')
def about():
    return render_template('public/about.html') 

@app.route('/search')
def search():
    query = request.args.get('q', '')
    return query

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
