# -*- coding: utf-8 -*-
from title import Title 
from description import Description 

class Job(object):

    def __init__(self, title = None, description = None):
        self.title       = title       or "Mangler tittel"
        self.description = description or "Mangler beskrivelse"

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @title.setter
    def title(self, title):
        if Title.isValid(title):
            self._title = Title.format(title)

    @description.setter
    def description(self, description):
        if Description.isValid(description):
            self._description = description
