# -*- coding: utf-8 -*-

class Board(object):

    sorters = {
        'title':    lambda job: job.title,
        'due_date': lambda job: job.due_date,
    }

    def __init__(self, jobs = [], sortBy = None):
        self._sortBy = sortBy
        self._jobs = jobs
        pass

    @property
    def jobs(self):
        if self._sortBy is not None and self._sortBy in Board.sorters:
            self._jobs.sort(key=Board.sorters[self._sortBy])

        return self._jobs 

