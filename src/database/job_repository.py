from sqlalchemy.sql     import text
from src.job.job        import Job
from company_repository import CompanyRepository 

class JobRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'jobs'
        self._companyRepository = CompanyRepository(database)

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, id))
        row = result.fetchone()
        if row is None: return None

        company = self._companyRepository.find(row.company_id)
        job = Job(
            id = row.id,
            title = row.title,
            description = row.description,
            due_date = row.due_date,
            company = company,
            place = row.place,
            position = row.position,
            start_date = row.start_date,
            status = row.status,
            edit_url = row.edit_url,
            apply_url = row.apply_url
        )
        return job

    def findAll(self):
        result = self._database.execute('select * from %s order by id desc' % (self._table))
        jobs = []
        for row in result:
            company = self._companyRepository.find(row.company_id)
            job = Job(
                id = row.id,
                title = row.title,
                description = row.description,
                due_date = row.due_date,
                company = company,
                place = row.place,
                position = row.position,
                start_date = row.start_date,
                status = row.status,
                edit_url = row.edit_url,
                apply_url = row.apply_url
            )
            jobs.append(job)
        return jobs

    def save(self, job):
        if job.id is None:
            return self.create(job)
        else:
            return self.update(job)

    def create(self, job):
        result = self._database.execute(text('insert into jobs set title = :title, description = :description, company_id = :company_id, position = :position, place = :place, due_date = :due_date, start_date = :start_date, status = :status, edit_url = :edit_url, apply_url = :apply_url'),
            table       = self._table,
            title       = job.title,
            description = job.description,
            company_id  = int(job.company.id),
            position    = job.position,
            place       = job.place,
            due_date    = job.due_date.date,
            start_date  = job.start_date.date,
            status      = job.status,
            edit_url    = job.edit_url,
            apply_url   = job.apply_url
        )
        job.id = result.lastrowid
        return job 

    def update(self, job):
        result = self._database.execute(text('update jobs set title = :title, description = :description, company_id = :company_id, position = :position, place = :place, due_date = :due_date, start_date = :start_date, apply_url = :apply_url, status = :status where id = :id'),
            table       = self._table,
            title       = job.title,
            description = job.description,
            company_id  = int(job.company.id),
            position    = job.position,
            place       = job.place,
            due_date    = job.due_date.date,
            start_date  = job.start_date.date,
            id          = job.id,
            status      = job.status,
            apply_url   = job.apply_url
        )
        return self.find(job.id)

    def remove(self, id):
        result = self._database.execute(text('delete from jobs where id = :id'), 
            id = id 
        )
