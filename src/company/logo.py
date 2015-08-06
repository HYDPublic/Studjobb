# -*- coding: utf-8 -*-
import os
from dimensions import dimensions

class LogoException(Exception):
    pass

class Logo(object):
    
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
            raise LogoException('Logo does not exist.')
        
        try:
            width, height, mime = dimensions(logoPath)[:3]
            if Logo.isTooWide(width):
                raise LogoException("Logo is too wide.")
            elif Logo.isTooHigh(height):
                raise LogoException("Logo is too high.")
        except NotImplementedError:
            raise LogoException("Could not parse logo format.")

        return True
