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
    
    def enqueue(self, mail, when):
        self._queue.append(SchedueledEntry(mail, when))

    def remove_duplicates(self):
        self._queue = list(set(self._queue))

    def mails_to_be_sent_now(self, now = datetime.datetime.now()):
        return filter(lambda schedueled_entry: schedueled_entry.when < now, self._queue)

    def send(self, now = datetime.datetime.now()):
        for schedueled_mail in self.mails_to_be_sent_now(now = now):
            mail = self._queue.pop(self._queue.index(schedueled_mail))

            # Pass on to mail library. This is not implemented yet, obviously.
            # It's quite difficult to test. A good idea is to
            # easily mock out the depedency to avoid emails actually being sent.

