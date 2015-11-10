# -*- coding: utf-8 -*-
import unittest 
import mock

from src.company.logo.logo import LogoException 
from src.company.logo.logo import LogoDownloader

class TestLogoDownloader(unittest.TestCase):

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
