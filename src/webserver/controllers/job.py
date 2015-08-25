from controller import Controller

from src.job.job import Job 
from src.job.status import Status 
from src.company.company import Company 
from src.database.job_repository import JobRepository
from src.database.company_repository import CompanyRepository
from src.webserver.authentication import Authentication

class JobController(Controller):
    
    def __init__(self, database):
        self.authentication = Authentication(database)
        self.company_repository = CompanyRepository(database) 
        self.job_repository = JobRepository(database) 
        super(JobController, self).__init__()

    def new(self):
        companies = self.company_repository.findAll()
        return self.render('admin/job/new.html', companies = companies) 

    def edit(self, id):
        job = self.job_repository.find(id)
        if not job:
            return self.abort(404)

        companies = self.company_repository.findAll()
        return self.render('admin/job/edit.html',
            job = job, companies = companies, statuses  = Status.codes) 

    def view(self, id):
        job = self.job_repository.find(id)
        if not job: return self.abort(404)
        return self.render('public/job.html', job = job)

    def create(self):
        job             = Job() 
        job.company     = self.company_repository.find(self.request.form['company'])
        job.title       = self.request.form.get('title')
        job.place       = self.request.form.get('place')
        job.due_date    = self.request.form.get('due_date')
        job.start_date  = self.request.form.get('start_date')
        job.position    = self.request.form.get('position')
        job.description = self.request.form.get('description')
        job = self.job_repository.save(job)
        return self.redirect(self.url_for('job.edit', id = job.id))

    def update(self, id):
        job = self.job_repository.find(id)
        company = self.company_repository.find(self.request.form['company'])

        job.title       = self.request.form.get('title')
        job.status      = self.request.form.get('status')
        job.description = self.request.form.get('description')
        job.due_date    = self.request.form.get('due_date')
        job.start_date  = self.request.form.get('start_date')
        job.position    = self.request.form.get('position')
        job.place       = self.request.form.get('place')
        job.company     = company 

        self.job_repository.save(job)
        return self.redirect(self.url_for('job.edit', id = id))