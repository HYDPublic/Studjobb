import unittest
from mock import MagicMock
from datetime import datetime, timedelta
from src.throttle.sentence import Sentence

class TestSentence(unittest.TestCase):

    def test_has_no_crime_by_default(self):
        assert Sentence().crimes == []

    def test_time_is_zero_if_no_crimes_are_comitted(self):
        assert Sentence().time.seconds == 0

    def test_time_is_same_as_crimes_punishment_when_one_crime_is_commited(self):
        sentence = Sentence()
        crime = MagicMock()
        crime.punishment = timedelta(hours = 5)
        sentence.add_crime(crime)
        assert sentence.time.seconds == (5 * 60 * 60)

    def test_time_is_the_sum_of_all_the_punishments(self):
        sentence = Sentence()
        first_crime, second_crime = MagicMock(), MagicMock()
        first_crime.punishment = timedelta(hours = 5)
        second_crime.punishment = timedelta(hours = 15)
        sentence.add_crime(first_crime)
        sentence.add_crime(second_crime)
        assert sentence.time.seconds == (20 * 60 * 60)
