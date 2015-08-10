# -*- coding: utf-8 -*-
import datetime
from title import Title 
from description import Description 

class Job(object):

    def __init__(self, id = None, title = None, description = None, due_date = None, company = None):
        self.id          = None
        self.title       = title       or "Mangler tittel"
        self.description = description or "Mangler beskrivelse"
        self.due_date    = due_date    or Job.dateThirtyDaysFromToday()
        self.company     = company

    @property
    def expired(self):
        return Job.dateToday() > self.due_date 

    @property
    def due_date(self):
        return self._due_date

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
        self._due_date = due_date 

    @company.setter
    def company(self, company):
        self._company = company 

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
