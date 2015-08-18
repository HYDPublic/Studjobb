# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 
from src.job.job import JobException
from src.job.start_date import StartDate 
from src.job.start_date import StartDateException

class TestJobStartDate(unittest.TestCase):

    def test_start_date_can_be_provided_as_a_ddmmyyy_string(self):
        start_date = StartDate(date = '2016-08-30')
        self.assertEqual(start_date.date, datetime.date(2016, 8, 30))

    def test_start_date_raises_error_if_format_is_wrong(self):
        self.assertRaisesRegexp(StartDateException, 'parse', StartDate, date = 'Tuesday 21th January 2016')

    def test_start_date_is_none_by_default(self):
        self.assertEqual(StartDate().date, None)

    def test_due_date_can_be_set_to_a_valid_date(self):
        five_days_from_now = datetime.timedelta(days=5)
        delta = datetime.date.today() + five_days_from_now
        start_date = StartDate(date = delta)
        self.assertEqual(start_date.date, delta)
