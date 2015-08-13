# -*- coding: utf-8 -*-

class Board(object):

    def __init__(self, jobs = [], sortByAttribute = None, filterExpiredJobs = True):
        self._jobs              = jobs
        self._sortByAttribute   = sortByAttribute
        self._filterExpiredJobs = filterExpiredJobs

    supportedAttributesToSortOn = {
        'title':    lambda job: job.title,
        'due_date': lambda job: job.due_date,
    }

    def sort(self, attributeToSortOn):
        self._jobs.sort(key=Board.supportedAttributesToSortOn[attributeToSortOn])

    def filterExpiredJobs(self):
        self._jobs = filter(lambda job: job.expired == False, self._jobs)

    @property
    def jobs(self):
        if self._sortByAttribute in Board.supportedAttributesToSortOn:
            self.sort(self._sortByAttribute)
        
        if self._filterExpiredJobs is True:
            self.filterExpiredJobs()

        return self._jobs 

    def jobs_by_status(self, status):
        jobs_with_provided_status = []
        for job in self._jobs:
            if job.status == status:
                jobs_with_provided_status.append(job)
        return jobs_with_provided_status
