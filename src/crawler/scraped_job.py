from bs4 import BeautifulSoup
from urlparse import urlparse
from src.job.job import Job


class ScrapedJob(Job):

    def __init__(self, *args, **kwargs):
        if 'guid'   in kwargs: self.guid   = kwargs.pop('guid')
        if 'url'    in kwargs: self.url    = kwargs.pop('url')
        if 'source' in kwargs: self.source = kwargs.pop('source')
        super(ScrapedJob, self).__init__(*args, **kwargs)

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        title = self.sanitizeHTML(title)
        self._title = title

    @staticmethod
    def sanitizeHTML(html):
        return BeautifulSoup(html, 'html.parser').getText()
