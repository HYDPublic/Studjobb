# -*- coding: utf-8 -*-
from title import Title 

class Job(object):

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if Title.isValid(title):
            self._title = Title.format(title)
