# -*- coding: utf-8 -*-
import datetime

class StartDateException(Exception):
    pass

class StartDate(object):
    
    def __init__(self, date = None):
        date = None if date == "" else date

        if isinstance(date, basestring):
            date = StartDate.convertStringToDate(date)

        self._date = date 

    @property
    def date(self):
        return self._date

    def is_before(self, date):
        if date == None:
            return True
        else:
            return self.date < date

    @staticmethod
    def convertStringToDate(date_as_string):
        try:
            return datetime.datetime.strptime(date_as_string, '%Y-%m-%d').date()
        except ValueError:
            raise StartDateException('Could not parse date.')
