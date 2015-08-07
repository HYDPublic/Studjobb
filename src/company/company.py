# -*- coding: utf-8 -*-
from logo import Logo
from name import Name

class Company(object):

    def __init__(self, name = None, logoPath = None):
        self.name = name or 'Mangler navn'
        self.logo = logoPath

    @property
    def name(self):
        return self._name 

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logoPath):
        self._logo = Logo(logoPath) 

    @name.setter
    def name(self, name):
        if Name.isValid(name):
            self._name = Name.format(name) 
