# -*- coding: utf-8 -*-
import unittest 
from mock import MagicMock
from src.crawler.website import Website 

class TestWebsite(unittest.TestCase):

    def test_website_raises_an_error_if_invalid_url(self):
        Website('Teknisk ukeblad', 'http://tu.no')
        with self.assertRaises(ValueError):
            Website('Teknisk ukeblad', 'htp://tu.no')

    def test_website_raises_an_error_if_missing_protocol(self):
        with self.assertRaises(ValueError):
            Website('Teknisk ukeblad', 'tu.no')

    def test_website_raises_an_error_if_url_does_not_start_with_protocol(self):
        with self.assertRaises(ValueError):
            Website('Teknisk ukeblad', 'hello.http://tu.no')

    def test_website_raises_an_error_if_url_is_missing_colon_and_dobule_dash(self):
        with self.assertRaises(ValueError):
            Website('Teknisk ukeblad', 'http!!!tu.no')

    def test_website_does_not_raise_error_if_protocol_is_https(self):
        Website('Teknisk ukeblad', 'https://tu.no')

    def test_website_has_no_pages_by_default(self):
        tu = Website('Teknisk ukeblad', 'https://tu.no')
        pages = tu.pages
        self.assertEqual(len(pages), 0)

    def test_website_can_have_a_page(self):
        tu = Website('Teknisk ukeblad', 'http://tu.no')
        page = MagicMock()
        tu.add_page(page)
        self.assertEqual(len(tu.pages), 1)
