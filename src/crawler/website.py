from urlparse import urlparse

class Website(object):

    def __init__(self, name, url):
        self._pages = []
        self.name = name

        if self.is_valid_url(url): 
            self.url = url
        else:
            raise ValueError('Invalid URL scheme.')

    @property
    def pages(self):
        return self._pages 

    def add_page(self, page):
        self._pages.append(1)
        pass

    @staticmethod
    def is_valid_url(url):
        url_parts = urlparse(url)
        return url_parts.scheme in ['http', 'https']
