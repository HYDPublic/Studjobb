# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.start_date import StartDate

class TestIsBefore(unittest.TestCase):

    def test_returns_true_if_start_date_is_before_date(self):
        start_date = StartDate(date = datetime.date(2015, 01, 1))
        self.assertEqual(start_date.is_before(datetime.date(2016, 1, 1)), True)
    
    def test_returns_false_if_start_date_is_same_as_date(self):
        start_date = StartDate(date = datetime.date(2015, 1, 1))
        self.assertEqual(start_date.is_before(datetime.date(2015, 1, 1)), False)

    def test_returns_false_if_start_date_is_after_date(self):
        start_date = StartDate(date = datetime.date(2015, 1, 1))
        self.assertEqual(start_date.is_before(datetime.date(2014, 1, 1)), False)
