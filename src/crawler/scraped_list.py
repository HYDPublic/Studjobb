
class ScrapedList(object):

    def __init__(self, scraped_jobs = []):
        self._scraped_jobs = scraped_jobs

    @property
    def scraped_jobs(self):
        return self._scraped_jobs

    @property
    def sources(self):
        sources = []
        for scraped_job in self._scraped_jobs:
            if scraped_job.source not in sources:
                sources.append(scraped_job.source)
        return sources 

    def scraped_jobs_from(self, source):
        scraped_jobs_matching_source = []
        for scraped_job in self._scraped_jobs:
            if scraped_job.source == source:
                scraped_jobs_matching_source.append(scraped_job)
        return scraped_jobs_matching_source 
