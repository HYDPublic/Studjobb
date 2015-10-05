# -*- coding: utf-8 -*-
import unittest 
import os
import mock

from src.company.logo.logo        import LogoException 
from src.company.logo.logopalette import LogoPalette 

class TestCompanyLogoPalette(unittest.TestCase):

    def test_logo_which_is_completely_red_will_almost_return_blue_as_the_most_dominant_color(self):
        pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        pathToRedLogo     = os.path.join(pathToDirWithLogo, '#ff0000-red-logo.png')
        red, green, blue  = LogoPalette(pathToRedLogo).color
        self.assertEqual(red   > 250, True)
        self.assertEqual(green < 5, True)
        self.assertEqual(blue  < 5, True)

    def test_logo_which_is_completely_blue_will_almost_return_blue_as_the_most_dominant_color(self):
        pathToDirWithLogo = os.path.abspath(os.path.join(__file__, '..', '..', 'fixtures'))
        pathToWhiteLogo   = os.path.join(pathToDirWithLogo, '#0000ff-blue-logo.png')
        red, green, blue  = LogoPalette(pathToWhiteLogo).color
        self.assertEqual(red   < 5, True)
        self.assertEqual(green < 5, True)
        self.assertEqual(blue  > 250, True)

    def test_logo_white_color_can_be_converted_to_hex_ffffff(self):
        rgb_color = (255, 255, 255)
        hex_color = LogoPalette.rgb_to_hex(rgb_color)
        self.assertEqual(hex_color, '#ffffff')

    def test_logo_black_color_can_be_converted_to_hex_000000(self):
        rgb_color = (0, 0, 0)
        hex_color = LogoPalette.rgb_to_hex(rgb_color)
        self.assertEqual(hex_color, '#000000')
