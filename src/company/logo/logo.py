# -*- coding: utf-8 -*-
import os

from dimensions     import dimensions
from logoexception  import LogoException
from logodownloader import LogoDownloader
from logorescaler   import LogoRescaler
from logoconfig     import LogoConfig

class Logo(object):

    def __init__(self, path):
        if path is not None:
            self.path = path 

    @property
    def url(self):
        return LogoConfig.urlToLogosFromConfig() + self.filename 

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

        path = os.path.abspath(os.path.join(LogoConfig.pathToStore(), path))

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
