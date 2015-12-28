# -*- coding: utf-8 -*-
from os.path import abspath, join
from urllib import urlencode
from ConfigParser import SafeConfigParser
from src.company.logo.search_engine_result import SearchEngineResult
from src.company.logo.search_engine import SearchEngine

class GoogleError(Exception):
    pass

class Google(SearchEngine):
    max_results = 5
    host = 'https://www.googleapis.com'
    query_string = '/customsearch/v1'

    def get_keys(self):
        config = SafeConfigParser()
        config.read(abspath(join(__file__, '..', '..', '..', '..', 'config')))
        return (config.get('google', 'cx'), config.get('google', 'api'))

    def extract_query_result(self, result):
        query_result = SearchEngineResult() 
        query_result.url = result['link']
        if result.has_key('image'):
            image = result['image']
            if image.has_key('height'):
                query_result.height = int(image['height'])
            if image.has_key('width'):
                query_result.width = int(image['width'])
        return query_result

    def convert_result_to_query_result(self, decoded_response):
        results = decoded_response['items']
        extracted_results = [self.extract_query_result(result) for result in results]
        return extracted_results[:Google.max_results:]

    def generate_query_url(self, query):
        keys = self.get_keys()
        query_parameters = {
            'q': query,
            'v': '1.0',
            'imgc': 'trans',
            'searchType': 'image',
            'imgSize': 'large',
            'alt': 'json',
            'num': '10',
            'start': '1',
            'key': keys[1],
            'cx': keys[0]
        }
        encoded_query_parameters = urlencode(query_parameters)
        return '{0}{1}?{2}'.format(self.host, self.query_string, encoded_query_parameters)

    def search(self, query):
        url = self.generate_query_url(query)
        response = self.request(url)
        decoded_response = self.json_decode_response(response)
        query_results = self.convert_result_to_query_result(decoded_response)
        return query_results
