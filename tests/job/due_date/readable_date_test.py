# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.due_date import DueDate

class TestReadableDate(unittest.TestCase):

    def test_human_readable_due_date_month_is_correct_for_january(self):
        due_date = DueDate(date = datetime.date(2015, 01, 1))
        self.assertEqual(due_date.human_readable_date, 'Jan 1')

    def test_human_readable_due_date_month_is_correct_for_february(self):
        due_date = DueDate(date = datetime.date(2015, 2, 2))
        self.assertEqual(due_date.human_readable_date, 'Feb 2')

    def test_human_readable_due_date_month_is_correct_for_march(self):
        due_date = DueDate(date = datetime.date(2015, 3, 3))
        self.assertEqual(due_date.human_readable_date, 'Mar 3')

    def test_human_readable_due_date_month_is_correct_for_april(self):
        due_date = DueDate(date = datetime.date(2015, 4, 4))
        self.assertEqual(due_date.human_readable_date, 'Apr 4')

    def test_human_readable_due_date_month_is_correct_for_may(self):
        due_date = DueDate(date = datetime.date(2015, 5, 5))
        self.assertEqual(due_date.human_readable_date, 'Mai 5')

    def test_human_readable_due_date_month_is_correct_for_june(self):
        due_date = DueDate(date = datetime.date(2015, 6, 6))
        self.assertEqual(due_date.human_readable_date, 'Jun 6')

    def test_human_readable_due_date_month_is_correct_for_july(self):
        due_date = DueDate(date = datetime.date(2015, 7, 7))
        self.assertEqual(due_date.human_readable_date, 'Jul 7')

    def test_human_readable_due_date_month_is_correct_for_august(self):
        due_date = DueDate(date = datetime.date(2015, 8, 8))
        self.assertEqual(due_date.human_readable_date, 'Aug 8')

    def test_human_readable_due_date_month_is_correct_for_september(self):
        due_date = DueDate(date = datetime.date(2015, 9, 9))
        self.assertEqual(due_date.human_readable_date, 'Sep 9')

    def test_human_readable_due_date_month_is_correct_for_october(self):
        due_date = DueDate(date = datetime.date(2015, 10, 10))
        self.assertEqual(due_date.human_readable_date, 'Okt 10')

    def test_human_readable_due_date_month_is_correct_for_november(self):
        due_date = DueDate(date = datetime.date(2015, 11, 11))
        self.assertEqual(due_date.human_readable_date, 'Nov 11')

    def test_human_readable_due_date_month_is_correct_for_december(self):
        due_date = DueDate(date = datetime.date(2015, 12, 24))
        self.assertEqual(due_date.human_readable_date, 'Des 24')
