# -*- coding: utf-8 -*-
import datetime

class ScheduelerError(Exception):
    pass

class SchedueledEmail(object):

    def __init__(self, email, when):
        self.email = email
        self.when  = when

    def __eq__(self, other_id):
        return self.email.id == other_id

    def __hash__(self):
        return self.email.id


class Schedueler(object):

    def __init__(self):
        self._queue = []

    @property
    def queue(self):
        return self._queue
    
    def enqueue(self, email, when):
        self._queue.append(SchedueledEmail(email, when))

    def remove_duplicates(self):
        self._queue = list(set(self._queue))

    def emails_to_be_sent_now(self, now = datetime.datetime.now()):
        return filter(lambda schedueled_email: schedueled_email.when < now, self._queue)

    def send(self, now = datetime.datetime.now()):
        for schedueled_email in self.emails_to_be_sent_now(now = now):
            email = self._queue.pop(self._queue.index(schedueled_email))

            # Pass on to email library
