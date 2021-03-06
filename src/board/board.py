# -*- coding: utf-8 -*-

class Board(object):

    def __init__(self, jobs = []):
        self._jobs = jobs

    supportedAttributes = {
        'title':    lambda job: job.title,
        'due_date': lambda job: job.due_date,
    }

    @property
    def jobs(self):
        return self._jobs 
    
    def jobs_by_status(self, status = None):
        return filter(lambda job: job.status == status, self._jobs)

    def jobs_sorted_by(self, attribute = None):
        try:
            sorting_key = Board.supportedAttributes[attribute]
        except KeyError:
            return self._jobs

        return sorted(self._jobs, key = sorting_key)
