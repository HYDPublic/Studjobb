from controller import Controller

from src.job.job import Job 
from src.job.status import Status 
from src.company.company import Company 
from src.database.job_repository import JobRepository
from src.database.company_repository import CompanyRepository

class JobController(Controller):
    
    def __init__(self, database):
        self.job_repository      = JobRepository(database) 
        self.company_repository  = CompanyRepository(database) 
        super(JobController, self).__init__()

    def get_job_from_request(self, job = None):
        job = job or Job()
        job.company     = self.company_repository.find(self.request.form['company'])
        job.title       = self.request.form.get('title')
        job.status      = self.request.form.get('status')
        job.description = self.request.form.get('description')
        job.due_date    = self.request.form.get('due_date')
        job.start_date  = self.request.form.get('start_date')
        job.position    = self.request.form.get('position')
        job.place       = self.request.form.get('place')
        job.apply_url   = self.request.form.get('apply_url')
        return job

    def new(self):
        companies = self.company_repository.findAll()
        return self.render('admin/job/new.html',
            companies = companies,
            statuses = Status.codes
        ) 

    @Controller.authentication_required
    def edit(self, id):
        job = self.job_repository.find(id)
        companies = self.company_repository.findAll()
        if not job:
            return self.abort(404)
        return self.render('admin/job/edit.html',
            job        = job,
            companies  = companies,
            statuses   = Status.codes
        ) 

    def preview(self, id, token):
        job = self.job_repository.find(id)
        if not job or job.edit_url != token:
            return self.abort(404)
        return self.render('public/job.html', job = job, logged_in = self.user_is_authenticated())

    def view(self, id):
        job = self.job_repository.find(id)
        published = job.status == 'active'
        if not job or not published:
            return self.abort(404)
        return self.render('public/job.html', job = job, logged_in = self.user_is_authenticated())

    @Controller.authentication_required
    def create(self):
        job = self.get_job_from_request()
        saved_job = self.job_repository.save(job)
        return self.redirect(self.url_for('job.edit', id = saved_job.id))

    @Controller.authentication_required
    def update(self, id):
        job = self.job_repository.find(id)
        updated_job = self.get_job_from_request(job)
        self.job_repository.save(updated_job)
        return self.redirect(self.url_for('job.edit', id = id))
