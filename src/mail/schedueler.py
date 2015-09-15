# -*- coding: utf-8 -*-
import datetime
from sender import Sender 
from schedueled_entry import SchedueledEntry

class ScheduelerError(Exception):
    pass

class Schedueler(object):

    def __init__(self, queue = None):
        self._queue = queue or []

    @property
    def queue(self):
        return self._queue
    
    def enqueue(self, mail, when):
        schedueled_entry = SchedueledEntry(mail, when)
        self._queue.append(schedueled_entry)

    def remove_duplicates(self):
        self._queue = list(set(self._queue))

    def mails_to_be_sent_now(self, now = datetime.datetime.now()):
        return filter(lambda schedueled_entry: schedueled_entry.when < now, self._queue)

    def send(self, now = datetime.datetime.now()):
        for schedueled_mail in self.mails_to_be_sent_now(now = now):
            index = self._queue.index(schedueled_mail)
            mail  = self._queue.pop(index)

            try:
                Sender(mail)
            except Exception:
                self._queue.append(mail)
