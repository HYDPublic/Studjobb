# -*- coding: utf-8 -*-
import os 
from logo import Logo

class LogoException(Exception):
    pass

class Company(object):

    def __init__(self, one = None, logoPath = None):
        self.logo = logoPath

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logoPath):
        if Logo.isValid(logoPath):
            self._logo = logoPath
