# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.job import Job 

class TestJobReadableDate(unittest.TestCase):

    def test_human_readable_due_date_month_is_correct_for_january(self):
        job = Job(due_date = datetime.date(2015, 01, 1))
        self.assertEqual(job.human_readable_due_date, 'Jan 1')

    def test_human_readable_due_date_month_is_correct_for_february(self):
        job = Job(due_date = datetime.date(2015, 2, 2))
        self.assertEqual(job.human_readable_due_date, 'Feb 2')

    def test_human_readable_due_date_month_is_correct_for_march(self):
        job = Job(due_date = datetime.date(2015, 3, 3))
        self.assertEqual(job.human_readable_due_date, 'Mar 3')

    def test_human_readable_due_date_month_is_correct_for_april(self):
        job = Job(due_date = datetime.date(2015, 4, 4))
        self.assertEqual(job.human_readable_due_date, 'Apr 4')

    def test_human_readable_due_date_month_is_correct_for_may(self):
        job = Job(due_date = datetime.date(2015, 5, 5))
        self.assertEqual(job.human_readable_due_date, 'Mai 5')

    def test_human_readable_due_date_month_is_correct_for_june(self):
        job = Job(due_date = datetime.date(2015, 6, 6))
        self.assertEqual(job.human_readable_due_date, 'Jun 6')

    def test_human_readable_due_date_month_is_correct_for_july(self):
        job = Job(due_date = datetime.date(2015, 7, 7))
        self.assertEqual(job.human_readable_due_date, 'Jul 7')

    def test_human_readable_due_date_month_is_correct_for_august(self):
        job = Job(due_date = datetime.date(2015, 8, 8))
        self.assertEqual(job.human_readable_due_date, 'Aug 8')

    def test_human_readable_due_date_month_is_correct_for_september(self):
        job = Job(due_date = datetime.date(2015, 9, 9))
        self.assertEqual(job.human_readable_due_date, 'Sep 9')

    def test_human_readable_due_date_month_is_correct_for_october(self):
        job = Job(due_date = datetime.date(2015, 10, 10))
        self.assertEqual(job.human_readable_due_date, 'Okt 10')

    def test_human_readable_due_date_month_is_correct_for_november(self):
        job = Job(due_date = datetime.date(2015, 11, 11))
        self.assertEqual(job.human_readable_due_date, 'Nov 11')

    def test_human_readable_due_date_month_is_correct_for_december(self):
        job = Job(due_date = datetime.date(2015, 12, 24))
        self.assertEqual(job.human_readable_due_date, 'Des 24')
