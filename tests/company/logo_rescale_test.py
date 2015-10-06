# -*- coding: utf-8 -*-
import unittest 
import os
import glob 
import mock
from PIL import Image

from src.company.logo.logo         import LogoException 
from src.company.logo.logorescaler import LogoRescaler

def clean_up_rescaled_images():
    pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
    for rescaledLogo in glob.iglob(os.path.join(pathToDirWithLogo, '*logo-rescaled*.png')):
        try:
            os.remove(rescaledLogo)
        except OSError:
            pass

def setUpModule():
    clean_up_rescaled_images() 

def tearDownModule():
    clean_up_rescaled_images() 

class TestLogoRescale(unittest.TestCase):

    def test_logo_width_can_be_resized_to_500px_from_501px(self):
        pathToDirWithLogo              = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        pathToLogoToBeRescaled         = os.path.join(pathToDirWithLogo, '501x500-logo-to-be-rescaled.png')
        pathToWhereRescaledLogoIsSaved = os.path.join(pathToDirWithLogo, '500x500-logo-rescaled-width.png')
        LogoRescaler.rescale(path = pathToLogoToBeRescaled, newPath = pathToWhereRescaledLogoIsSaved, width = 500)
        widthOfRescaledLogo = Image.open(pathToWhereRescaledLogoIsSaved).size[0]
        self.assertEqual(widthOfRescaledLogo, 500)

    def test_logo_height_can_be_resized_to_500px_from_501px(self):
        pathToDirWithLogo              = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        pathToLogoToBeRescaled         = os.path.join(pathToDirWithLogo, '500x501-logo-to-be-rescaled.png')
        pathToWhereRescaledLogoIsSaved = os.path.join(pathToDirWithLogo, '500x500-logo-rescaled-height.png')
        LogoRescaler.rescale(path = pathToLogoToBeRescaled, newPath = pathToWhereRescaledLogoIsSaved, height = 500)
        heightOfRescaledLogo = Image.open(pathToWhereRescaledLogoIsSaved).size[1]
        self.assertEqual(heightOfRescaledLogo, 500)
    
    @mock.patch('src.company.logo.logorescaler.LogoRescaler.save')
    def test_logo_rescaler_overwrites_original_logo_if_new_path_is_not_provided(self, mock_save_method):
        pathToDirWithLogo         = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        pathToLogoToBeOverwritten = os.path.join(pathToDirWithLogo, '500x501-logo-to-be-overwritten.png')
        LogoRescaler.rescale(path = pathToLogoToBeOverwritten, width = 500, height = 501)
        args, kwargs = mock_save_method.call_args
        self.assertEqual(args[1], pathToLogoToBeOverwritten)
