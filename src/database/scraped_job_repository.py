from sqlalchemy.sql          import text
from src.crawler.scraped_job import ScrapedJob

class ScrapedJobRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'scraped_jobs'

    def find(self, guid):
        result = self._database.execute(text('select * from scraped_jobs where guid = :guid and visible = true'), 
                guid = guid)
        row = result.fetchone()
        if row is None: return None

        scraped_job = ScrapedJob(
            guid = row.guid,
            title = row.title,
            description = row.description,
            due_date = row.due_date,
            company = row.company,
            source = row.source,
            url = row.url,
            scraped_at = row.scraped_at
        )
        return scraped_job

    def findAll(self):
        result = self._database.execute('select * from %s where visible = true order by scraped_at desc' % (self._table))
        scraped_jobs = []
        for row in result:
            scraped_job = ScrapedJob(
                guid = row.guid,
                title = row.title,
                description = row.description,
                due_date = row.due_date,
                company = row.company,
                source = row.source,
                url = row.url,
                scraped_at = row.scraped_at
            )
            scraped_jobs.append(scraped_job)
        return scraped_jobs 
    
    def save(self, scraped_job):
        result = self._database.execute(text('insert ignore into scraped_jobs set guid = :guid, title = :title, url = :url, source = :source, due_date = :due_date, description = :description, company = :company'),
            guid        = scraped_job.guid,
            url         = scraped_job.url,
            title       = scraped_job.title,
            description = scraped_job.description,
            company     = scraped_job.company,
            source      = scraped_job.source,
            due_date    = scraped_job.due_date
        )
        return scraped_job 

    def remove(self, guid):
        result = self._database.execute(text('update scraped_jobs set visible = false where guid = :guid'), guid = guid)
        return result
