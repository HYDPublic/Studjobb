# -*- coding: utf-8 -*-
import os
from os.path import join, abspath
from src.config.config import config
from dimensions     import dimensions
from logoexception  import LogoException
from logodownloader import LogoDownloader
from logorescaler   import LogoRescaler
from logopalette    import LogoPalette

class Logo(object):

    def __init__(self, path, color = None):
        self._color = color
        self.path   = path 

    @property
    def color(self):
        self.set_color_to_dominant_color_if_not_already_set()
        return self._color

    def set_color_to_dominant_color_if_not_already_set(self):
        if self._color is None:
            self._color = LogoPalette(self.path).color_in_hex

    @property
    def url(self):
        url = config.get('company_logo', 'url')
        return url + self.filename 

    @property
    def filename(self):
        head, tail = os.path.split(self._path) 
        return tail

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if LogoDownloader.isDownloadable(path):
            url = path
            path = LogoDownloader.download(url)

        path = abspath(join(config.get('company_logo', 'location'), path))

        if Logo.isValid(path):
            self._path = path
        
    @staticmethod
    def doesNotExist(logoPath):
        return os.path.isfile(logoPath) == False

    @staticmethod
    def isTooWide(width):
        return width > 500

    @staticmethod
    def isTooHigh(height):
        return height > 500
    
    @staticmethod
    def isValid(logoPath):
        if Logo.doesNotExist(logoPath):
            raise LogoException('Logo does not exist.', logoPath)
        
        try:
            # Try to parse image dimensions
            width, height = dimensions(logoPath)[:2]
        except NotImplementedError:
            raise LogoException("Could not parse logo format.")

        if Logo.isTooWide(width):
            LogoRescaler.rescale(path = logoPath, width = 500)
        elif Logo.isTooHigh(height):
            LogoRescaler.rescale(path = logoPath, height = 500)

        return True
