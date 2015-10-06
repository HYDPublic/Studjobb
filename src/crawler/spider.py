import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import requests
import urlparse
from hashlib import md5
from bs4 import BeautifulSoup 
from src.database.scraped_job_repository import ScrapedJobRepository
from src.database.engine import database

class Spider(object):

    user_agent = 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
    repository = ScrapedJobRepository(database)

    def __init__(self):
        print 'Loading {0} spider'.format(type(self).__name__)
        urls = self.collect_urls()
        for url in urls:
            if not self.has_visited_before(url):
                print '=> Visiting {0}'.format(url)
                response = self.visit_url(url).text
                scraped_job = self.scrape(url, response)
                self.repository.save(scraped_job)
                print '=> Saved data'

    def is_absolute(self, url):
        return bool(urlparse.urlparse(url).netloc)

    def selector(self, response_body, css_selector):
        soup = BeautifulSoup(response_body)
        return soup.select(css_selector)

    def request(self, url):
        return requests.get(url, headers = {
            'User-Agent': self.user_agent    
        }, proxies = {
#            'http': 'http://191.253.85.9:8080'
        })

    def extract_href(self, a_tag):
        return a_tag["href"] 

    def has_visited_before(self, url):
        guid = self.generate_guid(url)        
        return self.repository.find(guid)

    def generate_guid(self, url):
        return md5(url).hexdigest()

    def save(self, scraped_job):
        self.repository.save(scraped_job)
