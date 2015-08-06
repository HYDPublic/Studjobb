# -*- coding: utf-8 -*-
import unittest 
import os
from src.company.company import Company 
from src.company.company import LogoException 

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

