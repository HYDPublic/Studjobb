import unittest
from mock import MagicMock
from datetime import datetime, timedelta
from src.throttle.crime import Crime

class TestCrime(unittest.TestCase):

    def test_it_raises_exception_if_no_victim(self):
        with self.assertRaisesRegexp(Exception, 'victim'):
            Crime()

    def test_does_not_raise_exception_if_victim(self):
        crime = Crime(victim = 23)
        assert crime.victim == 23

    def test_it_has_a_default_punishment_of_0(self):
        crime = Crime(victim = 23)
        assert crime.punishment.seconds == 0

    def test_punishment_can_be_overriden_with_timedelta(self):
        crime = Crime(victim = 23, punishment = timedelta(hours = 14))
        assert crime.punishment.seconds == 14 * 60 * 60

    def test_punishment_can_not_have_a_negative_timedelta(self):
        crime = Crime(victim = 23, punishment = timedelta(hours = -1))
        assert crime.punishment.seconds == 0
