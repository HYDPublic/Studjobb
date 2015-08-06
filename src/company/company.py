# -*- coding: utf-8 -*-
import os 
from logo import Logo

class Company(object):

    def __init__(self, one = None, logoPath = None):
        self.logo = logoPath

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logoPath):

        if Logo.isURL(logoPath):
            logoPath = Logo.downloadFromURL(logoPath)

        if Logo.isValid(logoPath):
            self._logo = logoPath
