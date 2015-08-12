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
        company = self._companyRepository.find(row.company_id)
        job = Job(
            id = row.id,
            title = row.title,
            description = row.description,
            due_date = row.due_date,
            company = company,
            place = row.place,
            position = row.position
        )
        return job

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
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
                position = row.position
            )
            jobs.append(job)
        return jobs

    def save(self, job):
        if job.id is None:
            return self.create(job)
        else:
            return self.update(job)

    def create(self, job):
        result = self._database.execute(text('insert into jobs set title = :title, description = :description, company_id = :company_id, position = :position, place = :place'),
            table       = self._table,
            title       = job.title,
            description = job.description,
            company_id  = int(job.company.id),
            position    = job.position,
            place       = job.place
        )
        job.id = result.lastrowid
        return job 

    def update(self, job):
        result = self._database.execute(text('update jobs set title = :title, description = :description, company_id = :company_id, position = :position, place = :place where id = :id'),
            table       = self._table,
            title       = job.title,
            description = job.description,
            company_id  = int(job.company.id),
            position    = job.position,
            place       = job.place,
            id          = job.id
        )
        return self.find(job.id)

    def remove(self, job):
        pass
