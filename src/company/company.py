# -*- coding: utf-8 -*-
from logo.logo import Logo
from name      import Name

class Company(object):

    def __init__(self, id = None, name = None, logo = None):
        self.id   = id
        self.name = name or 'Mangler navn'
        self.logo = logo

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if Name.isValid(name):
            self._name = Name.format(name) 
