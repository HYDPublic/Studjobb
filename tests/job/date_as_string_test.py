# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.job import Job 
from src.job.job import JobException

class TestJobDateAsString(unittest.TestCase):

    def test_job_due_date_can_be_string(self):
        job = Job(due_date = datetime.date(2001, 1, 1))
        job.start_date = '2015-08-19'
