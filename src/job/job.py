# -*- coding: utf-8 -*-
import datetime
from title import Title 
from status import Status 
from due_date import DueDate 
from start_date import StartDate 
from description import Description 

class JobException(Exception):
    pass

class Job(object):

    def __init__(self, id = None, status = 'pending', title = 'Mangler tittel',
                 description = 'Mangler beskrivelse', due_date = None, start_date = None,
                 company = None, place = 'Ukjent', position = 'Ukjent'):

        self.id          = id 
        self.title       = title
        self.description = description 
        self.place       = place       
        self.position    = position    
        self.status      = status 
        self.due_date    = due_date
        self.start_date  = start_date
        self.company     = company

    @property
    def status(self):
        return unicode(self._status)

    @status.setter
    def status(self, status):
        self._status = Status(status)

    @property
    def expired(self):
        return self.due_date.remaining_days <= 0

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company 

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = Description(description)

    @property
    def title(self):
        return unicode(self._title)

    @title.setter
    def title(self, text):
        self._title = Title(text)

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        if hasattr(self, '_start_date') and self.start_date.is_before(due_date):
            raise JobException('Start date can not be before due date.')
        self._due_date = DueDate(due_date)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if start_date and self.due_date.is_after(start_date):
            raise JobException('Due date can not be after start date.')
        self._start_date = StartDate(start_date)
