# -*- coding: utf-8 -*-
from urllib import urlencode
from src.company.logo.search_engine_result import SearchEngineResult
from src.company.logo.search_engine import SearchEngine

class GoogleError(Exception):
    pass

class Google(SearchEngine):

    host = 'https://ajax.googleapis.com'
    query_string = '/ajax/services/search/images'

    def extract_query_result(self, result):
        query_result = SearchEngineResult() 
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

