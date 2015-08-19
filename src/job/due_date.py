# -*- coding: utf-8 -*-
import datetime

class DueDateException(Exception):
    pass

class DueDate(object):
    
    def __init__(self, date = None):

        if not date:
            date = DueDate.thirtyDaysFromNow()
        elif isinstance(date, basestring):
            date = DueDate.convertStringToDate(date)

        self._date = date 

    @property
    def date(self):
        return self._date

    @property
    def remaining_days(self):
        return max(0, (self._date - self.todaysDate()).days)

    @property
    def human_readable_date(self):
        human_readable_months = [
            'Januar', 'Februar', 'Marsj', 'April',
            'Mai', 'Juni', 'Juli', 'August',
            'September', 'Oktober', 'November', 'Desember'
        ]
        month = human_readable_months[self._date.month - 1]
        return '%s %d' % (month[:3], self._date.day)

    def is_after(self, date):
        if date == None:
            return True
        else:
            return self.date > date

    @staticmethod
    def todaysDate():
        return datetime.date.today()

    @staticmethod
    def thirtyDaysFromNow():
        return DueDate.todaysDate() + datetime.timedelta(days=30)

    @staticmethod
    def convertStringToDate(date_as_string):
        try:
            return datetime.datetime.strptime(date_as_string, '%Y-%m-%d').date()
        except ValueError:
            raise DueDateException('Could not parse date.')
