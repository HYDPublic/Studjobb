# -*- coding: utf-8 -*-
import datetime
from title import Title 
from description import Description 

class JobException(Exception):
    pass

class Job(object):

    def __init__(self, id = None, title = None, description = None, due_date = None,start_date = None, company = None, place = None, position = None):
        self.id          = id 
        self.title       = title       or "Mangler tittel"
        self.description = description or "Mangler beskrivelse"
        self.due_date    = due_date    or Job.dateThirtyDaysFromToday()
        self.start_date  = start_date
        self.company     = company
        self.place       = place       or "Ukjent"
        self.position    = position    or "Ukjent" 

    @property
    def expired(self):
        return Job.dateToday() > self.due_date 

    @property
    def due_date(self):
        return self._due_date

    @property
    def start_date(self):
        return self._start_date

    @property
    def company(self):
        return self._company

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

    @due_date.setter
    def due_date(self, due_date):
        if isinstance(due_date, basestring):
            due_date = Job.convertStringToDate(due_date)
        self._due_date = due_date 

    @start_date.setter
    def start_date(self, start_date):
        if start_date is '': start_date = None

        if isinstance(start_date, basestring):
            start_date = Job.convertStringToDate(start_date)
        
        if self.date_is_after_due_date(start_date):
            self._start_date = start_date 
        else:
            raise JobException('Start date must be after due date.')

    def date_is_after_due_date(self, date):
        if date is None:
            return True
        return date >= self._due_date

    @company.setter
    def company(self, company):
        self._company = company 

    @property
    def remaining_days_till_due_date(self):
        if self.expired:
            return False
        else:
            return (self._due_date - self.dateToday()).days

    @property
    def human_readable_due_date(self):
        human_readable_months = [
            'Januar', 'Februar', 'Marsj', 'April',
            'Mai', 'Juni', 'Juli', 'August',
            'September', 'Oktober', 'November', 'Desember'
        ]
        month = human_readable_months[self._due_date.month - 1]
        month_slug = month[:3]
        month_and_day = '%s %d' % (month_slug, self._due_date.day)
        return month_and_day

    @staticmethod
    def dateToday():
        return datetime.date.today()

    @staticmethod
    def dateThirtyDaysFromToday():
        return Job.dateToday() + datetime.timedelta(days=30)

    @staticmethod
    def convertStringToDate(date_as_string):
        try:
            return datetime.datetime.strptime(date_as_string, '%Y-%m-%d').date()
        except ValueError:
            raise JobException("Could not parse date.")
