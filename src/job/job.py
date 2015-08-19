# -*- coding: utf-8 -*-
import datetime
import uuid
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
                 company = None, place = 'Ukjent', position = 'Ukjent', edit_url = None):

        self.id          = id 
        self.title       = title
        self.description = description 
        self.place       = place       
        self.position    = position    
        self.status      = status 
        self.due_date    = due_date
        self.start_date  = start_date
        self.company     = company
        self.edit_url    = edit_url

    @property
    def edit_url(self):
        return self._edit_url

    @edit_url.setter
    def edit_url(self, url):
        self._edit_url = url or uuid.uuid4().hex

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
    def due_date(self, date):
        due_date = DueDate(date = date) 

        if date and hasattr(self, '_start_date') and self._start_date.date and self.start_date.is_before(due_date.date):
            raise JobException('Start date (%s) can not be before due date (%s).' %
            (self.start_date.date.strftime("%B %d, %Y"), due_date.date.strftime("%B %d, %Y")))

        self._due_date = due_date

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, date):
        start_date = StartDate(date = date)

        if date and self.due_date.is_after(start_date.date):
            raise JobException('Due date (%s) can not be after start date (%s).' %
            (self.due_date.date.strftime("%B %d, %Y"), start_date.date.strftime("%B %d, %Y")))

        self._start_date = start_date
