# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.mail.best_send_date import BestSendDate 

def ignore_time(date):
    return date.replace(hour=0, minute=0, second=0)

class TestBestSendDate(unittest.TestCase):

    def test_next_monday_returns_a_date_that_falls_on_monday(self):
        monday = datetime.datetime(2015, 9, 28)
        next_date = BestSendDate().next_date_for_weekday(monday, 'monday')
        self.assertEqual(next_date, monday)

    def test_next_wednesday_returns_a_date_that_falls_on_wednesday(self):
        tuesday   = datetime.datetime(2015, 9, 29)
        wednesday = datetime.datetime(2015, 9, 30)
        next_date = BestSendDate().next_date_for_weekday(tuesday, 'wednesday')
        self.assertEqual(next_date, wednesday)

    def test_next_friday_returns_a_date_that_falls_on_friday(self):
        sunday = datetime.datetime(2015,  9, 27)
        friday = datetime.datetime(2015, 10, 02)
        next_date = BestSendDate().next_date_for_weekday(sunday, 'friday')
        self.assertEqual(next_date, friday)

    def test_returns_monday_if_currently_sunday(self):
        sunday = datetime.datetime(2015, 10, 04)
        monday = datetime.datetime(2015, 10, 05)
        self.assertEqual(ignore_time(BestSendDate(now = sunday).date), monday)

    def test_returns_monday_if_currently_saturday(self):
        saturday = datetime.datetime(2015, 10, 03)
        monday   = datetime.datetime(2015, 10, 05)
        self.assertEqual(ignore_time(BestSendDate(now = saturday).date), monday)

    def test_returns_tuesday_if_currently_monday_three_o_clock(self):
        monday_three_o_clock = datetime.datetime(2015, 10, 05, 15, 00)
        tuesday = datetime.datetime(2015, 10, 06)
        best_date = BestSendDate(now = monday_three_o_clock)
        self.assertEqual(ignore_time(best_date.date), tuesday)

    def test_returns_monday_if_currently_monday_two_o_clock(self):
        monday_two_o_clock = datetime.datetime(2015, 10, 05, 14, 00)
        monday = datetime.datetime(2015, 10, 05)
        best_date = BestSendDate(now = monday_two_o_clock)
        self.assertEqual(ignore_time(best_date.date), monday)

    def test_returns_friday_if_currently_friday(self):
        friday  = datetime.datetime(2015, 9, 02)
        self.assertEqual(BestSendDate(now = friday).date, friday)

    def test_returns_monday_if_currently_friday_three_o_clock(self):
        friday_three_o_clock = datetime.datetime(2015, 10, 02, 15, 00)
        monday = datetime.datetime(2015, 10, 05)
        best_date = BestSendDate(now = friday_three_o_clock)
        self.assertEqual(ignore_time(best_date.date), monday)

    def test_time_is_not_adjusted_if_prior_to_threshold_on_a_thursday(self):
        thursday_one_o_clock = datetime.datetime(2015, 10, 01, 13, 13)
        best_date = BestSendDate(now = thursday_one_o_clock)
        self.assertEqual(best_date.date, thursday_one_o_clock)

    def test_time_is_adjusted_if_past_minute_threshold_on_a_thursday(self):
        thursday_one_o_clock = datetime.datetime(2015, 10, 01, 15, 00)
        best_date = BestSendDate(now = thursday_one_o_clock)
        self.assertNotEqual(best_date.date, thursday_one_o_clock)
