# -*- coding: utf-8 -*-
from urllib import urlencode
import json
import requests
from src.company.logo.logoexception import LogoException

class SearchEngineError(Exception):
    pass

class GoogleError(Exception):
    pass

class SearchEngine(object):

    def request(self, url):
        response = requests.get(url)
        if not response.ok:
            raise SearchEngineError('Search engine returned server error.')
        return response.text

    def json_decode_response(self, response):
        try: 
            return json.loads(response)
        except ValueError:
            raise SearchEngineError('JSON could not be decoded.')

class QueryResult(object):
    url = None 
    width = None
    height = None

class Google(SearchEngine):

    host = 'https://ajax.googleapis.com'
    query_string = '/ajax/services/search/images'

    def extract_query_result(self, result):
        query_result = QueryResult() 
        query_result.url = result['url']
        if result.has_key('height'):
            query_result.height = int(result['height'])
        if result.has_key('width'):
            query_result.width = int(result['width'])
        return query_result

    def convert_result_to_query_result(self, decoded_response):
        results = decoded_response['responseData']['results']
        return [self.extract_query_result(result) for result in results]

    def generate_query_url(self, query):
        query_parameters = {'q': query, 'v': '1.0', 'imgc': 'trans'}
        encoded_query_parameters = urlencode(query_parameters)
        return '{0}{1}?{2}'.format(self.host, self.query_string, encoded_query_parameters)

    def search(self, query):
        url = self.generate_query_url(query)
        response = self.request(url)
        decoded_response = self.json_decode_response(response)
        query_results = self.convert_result_to_query_result(decoded_response)
        return query_results

class LogoFinder(object):

    def __init__(self, query):
        if self.is_valid_query(query):
            self.query = query

    def search(self, search_engine):
        return search_engine.search(self.query)

    def is_valid_query(self, query):
        if not query:
            raise LogoException('Query can not be empty.')
        elif len(query) > 100:
            raise LogoException('Query is too long.')
        else:
            return True
