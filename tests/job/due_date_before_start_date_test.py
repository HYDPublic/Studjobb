# -*- coding: utf-8 -*-
import unittest 
import datetime
import mock
from src.job.job import Job 
from src.job.job import JobException

class TestJobDueDateBeforeStartDate(unittest.TestCase):

    def test_job_raises_exception_if_start_date_is_before_due_date_in_constructor(self):
        with self.assertRaisesRegexp(JobException, 'after'):
            Job(due_date = datetime.date(2000, 1, 1), start_date = datetime.date(1999, 1, 1))

    def test_job_raises_exception_if_start_date_is_before_due_date_in_setter(self):
        with self.assertRaisesRegexp(JobException, 'after'):
            job = Job(due_date = datetime.date(2000, 1, 1))
            job.start_date = datetime.date(1999, 1, 1)

    def test_job_raises_exception_if_due_date_is_after_start_date_in_setter(self):
        with self.assertRaisesRegexp(JobException, 'before'):
            job = Job(due_date = datetime.date(2000, 1, 1), start_date = datetime.date(2001, 1, 1))
            job.due_date = datetime.date(2005, 1, 1)

    def test_job_does_not_raise_exception_if_start_date_is_after_due_date(self):
        job = Job(due_date = datetime.date(1999, 1, 1))
        job.start_date = datetime.date(2000, 1, 1)

    def test_job_does_not_raise_exception_if_start_date_is_same_as_due_date(self):
        job = Job(due_date = datetime.date(2000, 1, 1))
        job.start_date = datetime.date(2000, 1, 1)

    @mock.patch("src.job.due_date.DueDate.todaysDate")
    def test_job_can_have_a_start_date_without_a_due_date_as_long_as_its_after(self, mock_date_today):
        mock_date_today.return_value = datetime.date(2000, 1, 1)
        job = Job(start_date = datetime.date(2001, 1, 1))
