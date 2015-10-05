# -*- coding: utf-8 -*-
from logo.logo import Logo
from name      import Name

class Company(object):

    def __init__(self, id = None, name = None, logo = None, color = None):
        self.id   = id
        self.name = name or 'Mangler navn'
        self.logo = { "path": logo, "color": color }

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name 

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, args):
        self._logo = Logo(path = args["path"], color = args["color"]) 

    @name.setter
    def name(self, name):
        if Name.isValid(name):
            self._name = Name.format(name) 
