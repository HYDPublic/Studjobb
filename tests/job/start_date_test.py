# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 
from src.job.job import JobException

class TestJobStartDate(unittest.TestCase):

    def test_job_has_none_as_default_start_date(self):
        self.assertEqual(Job().start_date, None)

    def test_job_start_date_can_be_set_to_none(self):
        job = Job()
        job.start_date = None

    def test_job_start_date_can_be_provided_as_a_ddmmyyy_string(self):
        job = Job(start_date = '2017-09-29')
        self.assertEqual(job.start_date, datetime.date(2017, 9, 29))

    def test_job_due_date_raises_error_if_format_is_wrong(self):
        self.assertRaisesRegexp(JobException, 'date', Job, due_date = 'Saturday 10th January 2013')

    def test_start_date_can_be_set_to_any_date(self):
        five_days_from_now = datetime.timedelta(days=5)
        delta = datetime.date.today() + five_days_from_now
        job = Job(start_date = delta)
        self.assertEqual(job.start_date, delta)
