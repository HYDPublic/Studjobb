from src.crawler.scraped_list import ScrapedList
from scraped_job_repository  import ScrapedJobRepository 

class ScrapedListRepository(object):

    def __init__(self, database):
        self._database = database

    def find(self):
        scraped_job_repository = ScrapedJobRepository(self._database)
        scraped_jobs = scraped_job_repository.findAll()
        return ScrapedList(scraped_jobs = scraped_jobs)

    def save(self):
        pass

    def remove(self):
        pass
