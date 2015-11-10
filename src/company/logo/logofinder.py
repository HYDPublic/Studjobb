# -*- coding: utf-8 -*-
from src.company.logo.google import Google, GoogleError
from src.company.logo.logoexception import LogoException

class LogoFinder(object):

    def __init__(self, query):
        if self.is_valid_query(query):
            self.query = query

    def search(self, search_engine):
        return search_engine.search(self.query)

    def is_valid_query(self, query):
        if not query:
            raise LogoException('Query can not be empty.')
        elif len(query) > 100:
            raise LogoException('Query is too long.')
        else:
            return True
