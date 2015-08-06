# -*- coding: utf-8 -*-
import os 
from dimensions import dimensions

class LogoException(Exception):
    pass

class Company(object):

    def __init__(self, one = None, logoPath = None):

        # Image existence
        if os.path.isfile(logoPath) == False:
            raise LogoException("File does not exist.")
        
        # Image dimensions
        try:
            width, height, mime = dimensions(logoPath)[:3]
        except:
            raise LogoException("Could not parse logo format.")

        if width  > 500: raise LogoException("Logo is too wide.")
        if height > 500: raise LogoException("Logo is too high.")
