# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 
from src.job.job import JobException

class TestJobDueDateBeforeStartDate(unittest.TestCase):

    def test_job_raises_exception_if_start_date_is_before_due_date(self):
        job = Job(due_date = datetime.date(2000, 1, 1))
        with self.assertRaisesRegexp(JobException, 'after'):
            job.start_date = datetime.date(1999, 1, 1)

    def test_job_does_not_raise_exception_if_start_date_is_after_due_date(self):
        job = Job(due_date = datetime.date(1999, 1, 1))
        job.start_date = datetime.date(2000, 1, 1)

    def test_job_does_not_raise_exception_if_start_date_is_same_as_due_date(self):
        job = Job(due_date = datetime.date(2000, 1, 1))
        job.start_date = datetime.date(2000, 1, 1)

