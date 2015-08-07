# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 

class TestJobDueDate(unittest.TestCase):

    def test_job_is_not_expired_by_default(self):
        self.assertEqual(Job().expired, False)

    def test_job_is_expired_if_date_is_in_past(self):
        job = Job(due_date=datetime.date(1993, 1, 1))
        self.assertEqual(job.expired, True)

    def test_job_is_not_expired_if_date_is_today(self):
        job = Job(due_date=datetime.date.today())
        self.assertEqual(job.expired, False)

    def test_due_date_is_30_days_by_default(self):
        thirty_days_from_now = datetime.timedelta(days=30)
        delta = datetime.date.today() + thirty_days_from_now
        self.assertEqual(Job().due_date, delta)

    def test_due_date_can_be_set_to_a_any_date(self):
        five_days_from_now = datetime.timedelta(days=5)
        delta = datetime.date.today() + five_days_from_now
        job = Job(due_date = delta)
        self.assertEqual(job.due_date, delta)

    @mock.patch("src.job.job.Job.dateToday")
    def test_due_date_works_on_new_years_eve(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2015, 12, 31)
        self.assertEqual(Job().due_date, datetime.date(2016, 01, 30))

    @mock.patch("src.job.job.Job.dateToday")
    def test_due_date_works_on_leap_year(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2016, 2, 29)
        self.assertEqual(Job().due_date, datetime.date(2016, 3, 30))
