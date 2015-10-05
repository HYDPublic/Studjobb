from colorthief import ColorThief
from logoexception import LogoException

class LogoPalette(object):

    def __init__(self, file):
        color_thief = ColorThief(file)
        self._color = color_thief.get_color(quality = 1)

    @property
    def color(self):
        return self._color

    @property
    def color_in_hex(self):
        return LogoPalette.rgb_to_hex(self.color)

    @staticmethod
    def rgb_to_hex(rgb_tuple):
        return '#%02x%02x%02x' % rgb_tuple 
