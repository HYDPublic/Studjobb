# -*- coding: utf-8 -*-
import requests
import json

class SearchEngineError(Exception):
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
