from sqlalchemy.sql          import text
from src.crawler.scraped_job import ScrapedJob

class ScrapedJobRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'scraped_jobs'

    def find(self, guid):
        result = self._database.execute(text('select * from scraped_jobs where guid = :guid'), 
                guid = guid)
        row = result.fetchone()
        if row is None: return None

        scraped_job = ScrapedJob(
            guid = row.guid,
            title = row.title,
            description = row.description,
            due_date = row.due_date,
            company = row.company
        )
        return scraped_job

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        scraped_jobs = []
        for row in result:
            scraped_job = ScrapedJob(
                guid = row.guid,
                title = row.title,
                description = row.description,
                due_date = row.due_date,
                company = row.company
            )
            scraped_jobs.append(scraped_job)
        return scraped_jobs 
    
    def save(self):
        pass

    def remove(self):
        pass
