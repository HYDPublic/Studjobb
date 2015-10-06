from controller import Controller

from src.job.job import Job 
from src.job.status import Status 
from src.company.company import Company 
from src.mail.best_send_date import BestSendDate 
from src.database.job_repository import JobRepository
from src.database.company_repository import CompanyRepository
from src.database.template_repository import TemplateRepository

class JobController(Controller):
    
    def __init__(self, database):
        self.job_repository      = JobRepository(database) 
        self.company_repository  = CompanyRepository(database) 
        self.template_repository = TemplateRepository(database) 
        super(JobController, self).__init__()

    def new(self):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        companies = self.company_repository.findAll()
        return self.render('admin/job/new.html', companies = companies, statuses = Status.codes) 

    def edit(self, id):
        if not self.user_is_authenticated(): return self.prompt_for_password()
        template_id      = self.request.args.get('template') or 1
        job              = self.job_repository.find(id)
        current_template = self.template_repository.find(template_id)
        if not job or not current_template:
            return self.abort(404)

        companies        = self.company_repository.findAll()
        templates        = self.template_repository.findAll()
        current_template.job = job

        return self.render('admin/job/edit.html',
            job                   = job,
            companies             = companies,
            templates             = templates,
            current_template      = current_template,
            statuses              = Status.codes,
            reccomended_send_date = BestSendDate()
        ) 

    def view(self, id):
        job = self.job_repository.find(id)
        if not job: return self.abort(404)
        return self.render('public/job.html', job = job)

    def create(self):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        job             = Job() 
        job.company     = self.company_repository.find(self.request.form['company'])
        job.title       = self.request.form.get('title')
        job.place       = self.request.form.get('place')
        job.due_date    = self.request.form.get('due_date')
        job.start_date  = self.request.form.get('start_date')
        job.position    = self.request.form.get('position')
        job.description = self.request.form.get('description')
        job.apply_url   = self.request.form.get('apply_url')
        job = self.job_repository.save(job)

        return self.redirect(self.url_for('job.edit', id = job.id))

    def update(self, id):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        job = self.job_repository.find(id)
        company = self.company_repository.find(self.request.form['company'])

        job.title       = self.request.form.get('title')
        job.status      = self.request.form.get('status')
        job.description = self.request.form.get('description')
        job.due_date    = self.request.form.get('due_date')
        job.start_date  = self.request.form.get('start_date')
        job.position    = self.request.form.get('position')
        job.place       = self.request.form.get('place')
        job.apply_url   = self.request.form.get('apply_url')
        job.company     = company 

        self.job_repository.save(job)
        return self.redirect(self.url_for('job.edit', id = id))
