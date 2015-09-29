# -*- coding: utf-8 -*-
import smtplib
import datetime
from mailer import Mailer 
from schedueled_entry import SchedueledEntry

class ScheduelerError(Exception):
    pass

class Schedueler(object):

    def __init__(self, queue = None):
        self._mailer    = Mailer()
        self._queue     = queue or []
        self.schedueled_entries_that_were_sent = []

    @property
    def queue(self):
        return self._queue
    
    def run(self, now = datetime.datetime.now()):
        for schedueled_mail in self.mails_to_be_sent_now(now = now):
            index            = self._queue.index(schedueled_mail)
            schedueled_entry = self._queue.pop(index)
            self.send(schedueled_entry);

    def mails_to_be_sent_now(self, now = datetime.datetime.now()):
        return filter(lambda schedueled_entry: schedueled_entry.when < now and schedueled_entry.sent == False, self._queue)

    def mark_as_sent(self, schedueled_entry):
        schedueled_entry.sent = True
        self.schedueled_entries_that_were_sent.append(schedueled_entry)

    def connect(self):
        self._mailer.connect()
        self._mailer.authenticate()

    def disconnect(self):
        self._mailer.disconnect()

    def send(self, schedueled_entry):
        try:
            self._mailer.send(schedueled_entry.mail)
            self.mark_as_sent(schedueled_entry)
        except smtplib.SMTPException:
            self._queue.append(schedueled_entry)
