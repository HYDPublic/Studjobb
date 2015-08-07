# -*- coding: utf-8 -*-
import os 
from logo import Logo

class Company(object):

    def __init__(self, logoPath = None):
        self.logo = logoPath

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logoPath):
        self._logo = Logo(logoPath) 
