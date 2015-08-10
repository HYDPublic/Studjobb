from src.job.job import Job

class JobRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'jobs'

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, id))
        row = result.fetchone()
        job = Job(id = row.id, title = row.title, description = row.description, due_date = row.due_date)
        return job

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        jobs = []
        for row in result:
            jobs.append(Job(id = row.id, title = row.title, description = row.description, due_date = row.due_date))
        return jobs

    def save(self, job):
        pass

    def remove(self, job):
        pass
