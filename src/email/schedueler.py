# -*- coding: utf-8 -*-
import datetime
from schedueled_entry import SchedueledEntry

class ScheduelerError(Exception):
    pass

class Schedueler(object):

    def __init__(self, queue = None):
        self._queue = queue or []

    @property
    def queue(self):
        return self._queue
    
    def enqueue(self, email, when):
        self._queue.append(SchedueledEntry(email, when))

    def remove_duplicates(self):
        self._queue = list(set(self._queue))

    def emails_to_be_sent_now(self, now = datetime.datetime.now()):
        return filter(lambda schedueled_entry: schedueled_entry.when < now, self._queue)

    def send(self, now = datetime.datetime.now()):
        for schedueled_email in self.emails_to_be_sent_now(now = now):
            email = self._queue.pop(self._queue.index(schedueled_email))

            # Pass on to email library
