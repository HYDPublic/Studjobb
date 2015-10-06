# -*- coding: utf-8 -*-
import unittest 
import os
import mock
from src.company.logo.logo    import LogoException 
from src.company.logo.logo    import Logo 
from src.company.logo.logo    import LogoDownloader

class TestLogo(unittest.TestCase):

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
        Logo(path = '500x500-logo.png')

    @mock.patch('src.company.logo.logo.LogoConfig.pathToStore')
    @mock.patch('src.company.logo.logo.LogoConfig.urlToLogosFromConfig')
    @mock.patch('src.company.logo.logo.Logo.isValid')
    def test_logo_has_property_for_where_to_reach_stored_logo_over_http(self, mock_isValid, mock_urlToLogosFromConfig, mock_pathToStore):
        mock_pathToStore.return_value = ""
        mock_isValid.return_value = True 
        mock_urlToLogosFromConfig.return_value = "http://website.no/logos/" 
        logoURL = Logo(path = "/Users/user/store/logos/here/wee.png").url
        self.assertEqual(logoURL, "http://website.no/logos/wee.png")

    @mock.patch('src.company.logo.logo.LogoPalette')
    @mock.patch('src.company.logo.logo.LogoConfig')
    @mock.patch('src.company.logo.logo.Logo.isValid')
    def test_logo_does_not_get_its_colors_extracted_if_color_is_supplied_in_constructor(self, mock_is_valid, mock_config, mock_logo_palette):
        mock_is_valid.return_value = True
        Logo(path = "", color = "#ffffff")
        assert not mock_logo_palette.called

    @mock.patch('src.company.logo.logo.LogoPalette')
    @mock.patch('src.company.logo.logo.LogoConfig')
    @mock.patch('src.company.logo.logo.Logo.isValid')
    def test_logo_does_get_its_colors_extracted_if_color_is_not_supplied_in_constructor(self, mock_is_valid, mock_config, mock_logo_palette):
        mock_is_valid.return_value = True
        Logo(path = "").color
        assert mock_logo_palette.called
