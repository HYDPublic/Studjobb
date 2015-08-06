# -*- coding: utf-8 -*-
import unittest 
import os
import mock
from src.company.company import Company 
from src.company.logo    import LogoException 
from src.company.logo    import Logo 

class TestCompanyLogo(unittest.TestCase):

    def test_logo_raises_error_if_file_does_not_exist(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', 'non-existent-logo.png'))
        self.assertRaisesRegexp(LogoException, 'not exist', Company, logoPath = pathToLogo)

    def test_logo_does_not_raise_error_if_file_does_exist(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', 'existent-logo.png'))
        Company(logoPath = pathToLogo)

    def test_logo_raises_error_if_wider_than_500px(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', '501x500-logo.png'))
        self.assertRaisesRegexp(LogoException, 'wide', Company, logoPath = pathToLogo)

    def test_logo_does_not_raise_error_if_width_is_smaller_than_500px(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', '500x500-logo.png'))
        Company(logoPath = pathToLogo)

    def test_logo_raises_error_if_higher_than_500px(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', '500x501-logo.png'))
        self.assertRaisesRegexp(LogoException, 'high', Company, logoPath = pathToLogo)

    @unittest.skip("dimensions uses stdout for errors, don't want to pollute test report.")
    def test_logo_raises_error_if_corrupt_image(self):
        pathToLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures', 'corrupted-logo.gif'))
        self.assertRaisesRegexp(LogoException, 'parse', Company, logoPath = pathToLogo)
    
    def test_logo_returns_true_if_url_is_provided(self):
        self.assertEqual(Logo.isURL("http://localhost:1337/logo-over-http.png"), True)

    def test_logo_returns_false_if_url_is_not_provided(self):
        self.assertEqual(Logo.isURL("/Users/user/logo-not-over-http.png"), False)

    def test_logo_returns_true_if_url_with_https_is_provided(self):
        self.assertEqual(Logo.isURL("https://localhost:1337/logo-over-http.png"), True)

    @mock.patch('src.company.logo.requests')
    def test_logo_calls_request_library_to_download_logo_from_url(self, mock_requests):
        urlToLogo = "http://localhost:1337/logo-over-http.png"
        Logo.downloadFromURL(urlToLogo)
        mock_requests.get.assert_called_with(urlToLogo)
