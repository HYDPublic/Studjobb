# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 
from src.job.job import JobException
from src.job.due_date import DueDate 
from src.job.due_date import DueDateException

class TestJobDueDate(unittest.TestCase):

    def test_due_date_can_be_provided_as_a_ddmmyyy_string(self):
        due_date = DueDate(date = '2016-08-30')
        self.assertEqual(due_date.date, datetime.date(2016, 8, 30))

    def test_due_date_raises_error_if_format_is_wrong(self):
        self.assertRaisesRegexp(DueDateException, 'parse', DueDate, date = 'Tuesday 21th January 2016')

    def test_due_date_is_30_days_by_default(self):
        thirty_days_from_now = datetime.timedelta(days=30)
        delta = datetime.date.today() + thirty_days_from_now
        self.assertEqual(DueDate().date, delta)

    def test_due_date_can_be_set_to_a_valid_date(self):
        five_days_from_now = datetime.timedelta(days=5)
        delta = datetime.date.today() + five_days_from_now
        due_date = DueDate(date = delta)
        self.assertEqual(due_date.date, delta)

    @mock.patch("src.job.due_date.DueDate.todaysDate")
    def test_default_due_date_works_on_new_years_eve(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2015, 12, 31)
        self.assertEqual(DueDate().date, datetime.date(2016, 01, 30))

    @mock.patch("src.job.due_date.DueDate.todaysDate")
    def test_default_due_date_works_on_leap_year(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2016, 2, 29)
        self.assertEqual(DueDate().date, datetime.date(2016, 3, 30))

    @mock.patch("src.job.due_date.DueDate.todaysDate")
    def test_days_till_due_date_is_one_when_one_day_till_due_date(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2016, 1, 1)
        due_date = DueDate(date = datetime.date(2016, 1, 2))
        self.assertEqual(due_date.remaining_days, 1)

    @mock.patch("src.job.due_date.DueDate.todaysDate")
    def test_days_till_due_date_is_0_when_due_date_is_in_the_past(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2016, 1, 2)
        due_date = DueDate(date = datetime.date(2016, 1, 1))
        self.assertEqual(due_date.remaining_days, 0)
