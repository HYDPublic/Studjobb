# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.due_date import DueDate

class TestIsAfter(unittest.TestCase):

    def test_returns_true_if_due_date_is_after_date(self):
        due_date = DueDate(date = datetime.date(2015, 01, 1))
        self.assertEqual(due_date.is_after(datetime.date(2014, 1, 1)), True)
    
    def test_returns_false_if_due_date_is_same_as_date(self):
        due_date = DueDate(date = datetime.date(2015, 1, 1))
        self.assertEqual(due_date.is_after(datetime.date(2015, 1, 1)), False)

    def test_returns_false_if_due_date_is_before_date(self):
        due_date = DueDate(date = datetime.date(2014, 1, 1))
        self.assertEqual(due_date.is_after(datetime.date(2015, 1, 1)), False)
