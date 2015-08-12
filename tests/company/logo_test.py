# -*- coding: utf-8 -*-
import unittest 
import os
import mock
from src.company.company      import Company 
from src.company.logo.logo    import LogoException 
from src.company.logo.logo    import Logo 
from src.company.logo.logo    import LogoDownloader

class TestCompanyLogo(unittest.TestCase):

    def test_logo_needs_not_to_be_provided_at_all(self):
        Company(logo = None)

    @mock.patch('src.company.logo.logo.LogoConfig.pathToStore')
    def test_logo_raises_error_if_file_does_not_exist(self, mock_path_to_store):
        pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        mock_path_to_store.return_value = pathToDirWithLogo
        self.assertRaisesRegexp(LogoException, 'not exist', Logo, path = 'non-existent-logo.png')

    @mock.patch('src.company.logo.logo.LogoConfig.pathToStore')
    def test_logo_does_not_raise_error_if_file_does_exist(self, mock_path_to_store):
        pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        mock_path_to_store.return_value = pathToDirWithLogo
        Logo(path = 'existent-logo.png')

    @mock.patch('src.company.logo.logo.LogoConfig.pathToStore')
    def test_logo_does_not_raise_error_if_width_is_smaller_than_500px(self, mock_path_to_store):
        pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        mock_path_to_store.return_value = pathToDirWithLogo
        Company(logo = '500x500-logo.png')

    def test_logo_downloader_returns_true_if_url_is_provided(self):
        url = "http://localhost:1337/logo-over-http.png"
        self.assertEqual(LogoDownloader.isDownloadable(url), True)

    def test_logo_downloader_returns_false_if_url_is_not_provided(self):
        url = "/Users/user/logo-not-over-http.png"
        self.assertEqual(LogoDownloader.isDownloadable(url), False)

    def test_logo_downloader_returns_true_if_url_with_https_is_provided(self):
        url = "https://localhost:1337/logo-over-http.png"
        self.assertEqual(LogoDownloader.isDownloadable(url), True)

    @mock.patch('src.company.logo.logodownloader.requests')
    def test_logo_downloader_calls_request_library_to_download_logo_from_url(self, mock_requests):
        url = "http://localhost:1337/logo-over-http.png"
        LogoDownloader.requestExternalImageOverHTTP(url)
        mock_requests.get.assert_called_with(url, stream=True)

    @mock.patch('src.company.logo.logodownloader.requests')
    def test_logo_raises_error_if_requests_could_not_complete(self, mock_request):
        class failedResponse:
            def __init__(self):
                self.ok = False 
        mock_request.get.return_value = failedResponse()
        self.assertRaisesRegexp(LogoException, 'download', LogoDownloader.download, "http://illegal-url.com")

    @mock.patch('src.company.logo.logoconfig.SafeConfigParser')
    def test_logo_generates_an_absolute_path_for_logo_based_on_config(self, mock_configParser):
        mock_configParser().get.return_value = "/Users/user/store/logos/here/"
        self.assertEqual("/Users/user/store/logos/here/" in LogoDownloader.generatePathForImage(), True)

    def test_logo_generates_a_unique_filename(self):
        firstFilename  = LogoDownloader.generateUniqueFilename()
        secondFilename = LogoDownloader.generateUniqueFilename()
        self.assertNotEqual(firstFilename, secondFilename)

    def test_logo_generates_a_unique_filename_with_extension_if_provided(self):
        filename = LogoDownloader.generateUniqueFilename(extension = 'png')
        self.assertEqual(filename.endswith('.png'), True)

    def test_logo_ignores_extension_if_none_is_provided(self):
        filename = LogoDownloader.generateUniqueFilename()
        self.assertEqual(filename.endswith('.png'), False)

    @mock.patch('__builtin__.open')
    def test_logo_gets_written_to_path(self, mock_open):
        LogoDownloader.writeTo("/Users/user/store/logos/here/logo.png", "imagedata")
        mock_open.assert_called_with("/Users/user/store/logos/here/logo.png", "wb")

    def test_logo_can_determine_extension_from_url(self):
        self.assertEqual(LogoDownloader.getExtensionFromURL('http://domain.com/logo.png'), 'png')
        self.assertEqual(LogoDownloader.getExtensionFromURL('http://domain.com/logo.gif'), 'gif')
        self.assertEqual(LogoDownloader.getExtensionFromURL('http://domain.com/logo.jpg'), 'jpg')

    @mock.patch('src.company.logo.logo.LogoConfig.pathToStore')
    @mock.patch('src.company.logo.logo.LogoConfig.urlToLogosFromConfig')
    @mock.patch('src.company.logo.logo.Logo.isValid')
    def test_logo_has_property_for_where_to_reach_stored_logo_over_http(self, mock_isValid, mock_urlToLogosFromConfig, mock_pathToStore):
        mock_pathToStore.return_value = ""
        mock_isValid.return_value = True 
        mock_urlToLogosFromConfig.return_value = "http://website.no/logos/" 
        logoURL = Logo(path = "/Users/user/store/logos/here/wee.png").url
        self.assertEqual(logoURL, "http://website.no/logos/wee.png")
