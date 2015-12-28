# -*- coding: utf-8 -*-
import unittest 
from mock import PropertyMock, MagicMock, patch

from src.company.logo.search_engine import SearchEngine, SearchEngineError
from src.company.logo.google import Google, GoogleError
from src.company.logo.logofinder import LogoFinder
from src.company.logo.logoexception import LogoException

class TestSearchEngine(unittest.TestCase):

    @patch('src.company.logo.search_engine.requests.get')
    def test_exception_is_thrown_if_response_is_not_ok(self, requests):
        type(requests.return_value).ok = PropertyMock(return_value=False)
        with self.assertRaisesRegexp(SearchEngineError, 'server error'):
            SearchEngine().request('http://search-engine.com?q=company+logo')

    def test_search_engine_raises_exception_if_malformed_json_response(self):
        search_engine = SearchEngine()
        response = '{": []}, reseDetails",,None, "onseStatus": WOW}'
        with self.assertRaisesRegexp(SearchEngineError, 'JSON'):
            search_engine.json_decode_response(response)

class TestGoogle(unittest.TestCase):

    def test_google_extracts_zero_query_results_from_zero_results(self):
        google = Google()
        decoded_response = {u'items': []}
        results = google.convert_result_to_query_result(decoded_response)
        assert len(results) == 0

    def test_google_extracts_one_query_result_from_one_result(self):
        google = Google()
        decoded_response = {u'items': [{
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'width': 250,
                u'height': 250
            }
        }]}
        results = google.convert_result_to_query_result(decoded_response)
        assert len(results) == 1

    def test_google_extracts_two_query_result_from_two_result(self):
        google = Google()
        item = {
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'width': 250,
                u'height': 250
            }
        }
        items = [item] * 2
        decoded_response = {u'items': items}
        results = google.convert_result_to_query_result(decoded_response)
        assert len(results) == 2

    def test_google_limits_results_to_five(self):
        google = Google()
        item = {
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'width': 250,
                u'height': 250
            }
        }
        items = [item] * 100
        decoded_response = {u'items': items}
        results = google.convert_result_to_query_result(decoded_response)
        assert len(results) == 5

    def test_google_can_extract_a_query_result_object_with_url_from_a_result(self):
        google = Google()
        item = {u'link': 'http://logo.com/logo.png'}
        query_result = google.extract_query_result(item)
        assert query_result.url == 'http://logo.com/logo.png'

    def test_google_can_extract_a_query_result_object_with_width_from_a_result(self):
        google = Google()
        item = {
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'width': 250,
                u'height': 500
            }
        }
        query_result = google.extract_query_result(item)
        assert query_result.width == 250

    def test_google_sets_query_result_width_to_none_if_missing_height_from_result(self):
        google = Google()
        item = {
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'width': 500,
            }
        }
        query_result = google.extract_query_result(item)
        assert query_result.height == None

    def test_google_can_extract_a_query_result_object_with_height_from_a_result(self):
        google = Google()
        item = {
            u'link': 'http://logo.com/logo.png',
            u'image': {
                u'height': 500,
                u'width': 500
            }
        }
        query_result = google.extract_query_result(item)
        assert query_result.height == 500

    def test_google_generates_a_url_with_query_as_get_parameter(self):
        google = Google()
        request_url = google.generate_query_url('sopra steria logo')
        assert 'sopra+steria+logo' in request_url

class TestLogoFinder(unittest.TestCase):

    def test_logo_finder_raises_exception_if_empty_query(self):
        with self.assertRaisesRegexp(LogoException, 'empty'):
            LogoFinder('')

    def test_logo_finder_raises_exception_query_is_over_100_characters(self):
        with self.assertRaisesRegexp(LogoException, 'long'):
            LogoFinder('char' * 26)

    def test_logo_finder_forwards_query_to_search_engine(self):
        google = MagicMock()
        results = LogoFinder('bekk logo').search(google)
        google.search.assert_called_with('bekk logo')

    def test_logo_finder_returns_two_results_if_search_engine_found_two_results(self):
        google = MagicMock()
        google.search.return_value = [MagicMock('QueryResult'), MagicMock('QueryResult')]
        results = LogoFinder('bouvet logo').search(google)
        assert len(results) == 2

    def test_logo_finder_returns_zero_results_if_search_engine_found_zero_results(self):
        google = MagicMock()
        google.search.return_value = []
        results = LogoFinder('ewdhewhwehfwef logo').search(google)
        assert len(results) == 0
