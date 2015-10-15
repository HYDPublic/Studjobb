from src.config.config import config
from urlparse import urlparse
import requests

class AlreadyVisitedError(Exception):
    pass

class Robot(object):

    def __init__(self):
        self.visited_urls = []

    @property
    def user_agent(self):
        return config('crawler', 'user_agent')

    @property
    def proxy(self):
        return config('crawler', 'proxy')

    def visit(self, url):
        if not Robot.is_valid_url(url):
            raise ValueError('Invalid URL provided.')
        if url in self.visited_urls:
            raise AlreadyVisitedError(url)
        return self.request(url)

    def request(self, url, method = 'GET'):
        arguments = {
            'url': url,
            'method': method,
            'headers': {
                'user-agent': self.user_agent 
            }
        }
        response = requests.request(**arguments)
        self.visited_urls.append(url)
        return response

    @staticmethod
    def is_valid_url(url):
        url_pieces = urlparse(url)
        return url_pieces.netloc and url_pieces.scheme
