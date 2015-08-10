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
            )
            jobs.append(job)
        return jobs

    def save(self, job):
        pass

    def remove(self, job):
        pass
