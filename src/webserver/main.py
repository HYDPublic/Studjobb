# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from flask import Flask
from flask import render_template
from flask import abort 
from flask import request
from flask import redirect 
from flask import send_from_directory
from flask.ext.httpauth import HTTPBasicAuth

from src.database.engine import database
from src.database.job_repository import JobRepository
from src.database.user_repository import UserRepository
from src.database.board_repository import BoardRepository
from src.database.company_repository import CompanyRepository
from src.database.scraped_job_repository import ScrapedJobRepository 
from src.database.scraped_list_repository import ScrapedListRepository

from src.job.job import Job 
from src.job.job import JobException
from src.job.title import TitleException
from src.company.company import Company
    
# Configuration
app  = Flask(__name__, template_folder = 'views', static_folder = 'assets')
auth = HTTPBasicAuth()

# Repositories
job_repository = JobRepository(database)
user_repository = UserRepository(database)
board_repository = BoardRepository(database)
company_repository = CompanyRepository(database)
scraped_job_repository = ScrapedJobRepository(database)
scraped_list_repository = ScrapedListRepository(database)

# Authentication
@auth.verify_password
def verify_pw(email, password):
    user = user_repository.find(email)
    if user is None:
        return False
    return user.checkCredentials(password)

@app.route('/sitemap.xml')
@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

# Routes
@app.route('/admin')
@auth.login_required
def admin():
    board        = board_repository.find()
    scraped_list = scraped_list_repository.find()

    return render_template('admin/admin.html', 
        scraped_jobs = scraped_list.scraped_jobs,
        active_jobs  = board.jobs_by_status('active'),
        pending_jobs = board.jobs_by_status('pending'),
        dead_jobs    = board.jobs_by_status('dead')
    )

@auth.login_required
@app.route('/admin/stilling/<int:id>', methods = ['GET'])
def edit_job(id):
    job = job_repository.find(id)
    companies = company_repository.findAll()
    return render_template('admin/job/edit.html',
        job       = job,
        companies = companies,
        statuses  = job.statuses
    ) 

@auth.login_required
@app.route('/admin/stilling/<int:id>', methods = ['POST'])
def save_job(id):

    if request.form.get('delete', False):
        job_repository.remove(id)
        return redirect('/admin')

    job       = job_repository.find(id)
    company   = company_repository.find(request.form['company'])
    companies = company_repository.findAll()

    try:
        job.title       = request.form.get('title')
        job.status      = request.form.get('status')
        job.description = request.form.get('description')
        job.due_date    = request.form.get('due_date')
        job.start_date  = request.form.get('start_date')
        job.position    = request.form.get('position')
        job.place       = request.form.get('place')
        job.company     = company 
    except (JobException, TitleException) as error:
        return render_template('admin/job/edit.html',
            statuses  = job.statuses,
            error     = error,
            job       = job,
            companies = companies
        ) 

    job = job_repository.save(job) 
    return render_template('admin/job/edit.html',
        job       = job,
        companies = companies,
        statuses  = job.statuses
    ) 

@auth.login_required
@app.route('/admin/selskap/<int:id>', methods = ['GET'])
def edit_company(id):
    company = company_repository.find(id)
    return render_template('admin/company/edit.html', company = company) 

@auth.login_required
@app.route('/admin/skrapt/<string:guid>', methods = ['GET'])
def edit_scraped_job(guid):
    scraped_job = scraped_job_repository.find(guid)
    if scraped_job == None:
        return abort(404)

    companies = company_repository.findAll()

    return render_template('admin/scraped_job/edit.html',
        scraped_job = scraped_job,
        companies   = companies 
    ) 

@auth.login_required
@app.route('/admin/selskap/<int:id>', methods = ['POST'])
def save_company(id):
    company = company_repository.find(id)
    company.name = request.form['name']
    company.logo = request.form['logo'].encode('utf8')
    company = company_repository.save(company) 
    return render_template('admin/company/edit.html', company = company) 

@auth.login_required
@app.route('/admin/stilling', methods = ['GET'])
def new_job():
    companies = company_repository.findAll()
    return render_template('admin/job/new.html', companies = companies) 

@auth.login_required
@app.route('/admin/stilling', methods = ['POST'])
def create_job():

    company    = Company()
    company.id = request.form.get('company')

    job             = Job() 
    job.company     = company
    job.title       = request.form.get('title')
    job.place       = request.form.get('place')
    job.due_date    = request.form.get('due_date')
    job.start_date  = request.form.get('start_date')
    job.position    = request.form.get('position')
    job.description = request.form.get('description')

    job = job_repository.save(job)
    return redirect('/admin/stilling/%d' % job.id)

@auth.login_required
@app.route('/admin/selskap', methods = ['GET'])
def new_company():
    companies = company_repository.findAll()
    return render_template('admin/company/new.html', companies = companies) 

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
    return render_template('public/index.html',
        jobs = board.jobs_by_status('active')
    ) 

@app.route('/stilling/<int:id>')
def job(id):
    job = job_repository.find(id)
    if job is None:
        return abort(404)
    else:
        return render_template('public/job.html',
            job = job, logged_in = auth.username()
        ) 

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
