import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.crawler.proxy_finder import ProxyFinder
from src.database.engine import database
from src.database.scraped_job_repository import ScrapedJobRepository

class Crawler(object):

    def __init__(self, formulas = [], debug = False):
        self.debug = debug
        self.proxy_ip = self.find_proxy()
        self.repository = ScrapedJobRepository(database)
        self.formulas = formulas
        self.headers  = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        }
        self.proxies  = {
#            'http': 'http://' + self.proxy_ip,
#            'https': 'http://' + self.proxy_ip
        }

    def find_proxy(self):
        if self.debug: print 'Finding proxy. This may take a while.'
        proxy_ip_address = ProxyFinder().find_proxy()
        if self.debug: print 'Proxy found: {0}'.format(proxy_ip_address)
        return proxy_ip_address

    def run(self):

        for formula in self.formulas:
            name = formula.__class__.__name__
            if self.debug: print 'Crawling {0}.'.format(name)

            # Get job urls for current formula
            job_urls = self.get_all_job_urls(formula)

            # Parse each job
            for job_url in job_urls:
                html = self.request(formula.session, job_url)
                scraped_job = formula.extract_job(job_url, html)
                self.debug_print(scraped_job)

                # Save each job
                if not self.debug:
                    self.repository.save(scraped_job)

    def debug_print(self, scraped_job):
        if self.debug:
            print u'URL: {0}'.format(scraped_job.url)
            print u'Title: {0}'.format(scraped_job.title)
            print u'Due date: {0}'.format(scraped_job.due_date)
            print u'Description: {0}'.format(scraped_job.description)
            print '\n'

    def get_all_job_urls(self, formula):
        if self.debug: print 'Looking for urls.'
        html = self.request(formula.session, formula.board_url)
        job_urls = formula.extract_job_urls(html)
        if self.debug: print 'Found {0} urls.'.format(len(job_urls))
        return job_urls

    def request(self, session, url):
        r = session.get(url,
            headers=self.headers,
            proxies=self.proxies
        )
        return r.text
