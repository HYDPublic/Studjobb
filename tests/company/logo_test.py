# -*- coding: utf-8 -*-
import unittest 
import os
import mock
from src.company.company import Company 
from src.company.logo    import LogoException 
from src.company.logo    import Logo 

class TestCompanyLogo(unittest.TestCase):


    def test_logo_needs_not_to_be_provided_at_all(self):
        Company(logoPath = None)

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
        Logo.requestExternalImageOverHTTP(urlToLogo)
        mock_requests.get.assert_called_with(urlToLogo, stream=True)

    @mock.patch('src.company.logo.requests')
    def test_logo_raises_error_if_requests_could_not_complete(self, mock_request):
        class failedResponse:
            def __init__(self):
                self.ok = False 
        mock_request.get.return_value = failedResponse()
        self.assertRaisesRegexp(LogoException, 'download', Logo.downloadFromURL, "http://illegal-url.com")

    @mock.patch('src.company.logo.SafeConfigParser')
    def test_logo_generates_an_absolute_path_for_logo_based_on_config(self, mock_configParser):
        mock_configParser().get.return_value = "/Users/user/store/logos/here/"
        self.assertEqual("/Users/user/store/logos/here/" in Logo.generatePathForImage(), True)

    def test_logo_generates_a_unique_filename(self):
        firstFilename  = Logo.generateUniqueFilename()
        secondFilename = Logo.generateUniqueFilename()
        self.assertNotEqual(firstFilename, secondFilename)

    def test_logo_generates_a_unique_filename_with_extension_if_provided(self):
        filename = Logo.generateUniqueFilename('png')
        self.assertEqual(filename.endswith('.png'), True)

    @mock.patch('__builtin__.open')
    def test_logo_gets_written_to_path(self, mock_open):
        Logo.writeTo("/Users/user/store/logos/here/logo.png", "imagedata")
        mock_open.assert_called_with("/Users/user/store/logos/here/logo.png", "wb")

    def test_logo_can_determine_extension_from_url(self):
        self.assertEqual(Logo.getExtensionFromURL('http://domain.com/logo.png'), 'png')
        self.assertEqual(Logo.getExtensionFromURL('http://domain.com/logo.gif'), 'gif')
        self.assertEqual(Logo.getExtensionFromURL('http://domain.com/logo.jpg'), 'jpg')

    @mock.patch('src.company.logo.Logo.urlToLogosFromConfig')
    @mock.patch('src.company.logo.Logo.isValid')
    def test_logo_has_property_for_where_to_reach_stored_logo_over_http(self, mock_isValid, mock_urlToLogosFromConfig):
        mock_isValid.return_value = True 
        mock_urlToLogosFromConfig.return_value = "http://website.no/logos/" 
        logoURL = Logo(path = "/Users/user/store/logos/here/wee.png").url
        self.assertEqual(logoURL, "http://website.no/logos/wee.png")
