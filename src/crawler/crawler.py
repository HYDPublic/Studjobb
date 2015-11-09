import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from src.crawler.proxy_finder import ProxyFinder
from src.database.engine import database
from src.database.scraped_job_repository import ScrapedJobRepository

class Crawler(object):

    def __init__(self, formulas = []):
        self.proxy_ip = ProxyFinder().find_proxy()
        self.repository = ScrapedJobRepository(database)
        self.formulas = formulas
        self.headers  = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        }
        self.proxies  = {
            'http': 'http://' + self.proxy_ip,
            'https': 'http://' + self.proxy_ip
        }

    def run(self):

        for formula in self.formulas:
            # Get job urls for current formula
            job_urls = self.get_all_job_urls(formula)

            # Parse each job
            for job_url in job_urls:
                html = self.request(formula.session, job_url)
                scraped_job = formula.extract_job(job_url, html)

                # Save each job
                self.repository.save(scraped_job)

    def get_all_job_urls(self, formula):
        html = self.request(formula.session, formula.board_url)
        job_urls = formula.extract_job_urls(html)
        return job_urls

    def request(self, session, url):
        r = session.get(url,
            headers=self.headers,
            proxies=self.proxies
        )
        return r.text
