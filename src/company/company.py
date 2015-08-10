# -*- coding: utf-8 -*-
from logo import Logo
from name import Name

class Company(object):

    def __init__(self, name = None, logo = None):
        self.name = name or 'Mangler navn'
        self.logo = logo

    @property
    def name(self):
        return self._name 

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logo):
        self._logo = Logo(logo) 

    @name.setter
    def name(self, name):
        if Name.isValid(name):
            self._name = Name.format(name) 
