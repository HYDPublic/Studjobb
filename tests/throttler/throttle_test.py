from mock import MagicMock 
import unittest
from src.throttler.throttler import Throttler

def mock_attempt(ip, user_id):
    attempt = MagicMock()
    attempt.user_id = user_id
    attempt.ip = ip
    attempt.identifier = (ip, user_id)
    return attempt

class TestThrottler(unittest.TestCase):

    def test_it_has_no_login_attempts_by_default(self):
        throttler = Throttler()
        assert throttler.get_total_number_of_login_attempts() == 0

    def test_it_can_add_a_login_attempt(self):
        throttler = Throttler()
        attempt = mock_attempt(ip = '88.126.21.23', user_id = 3)
        throttler.add_login_attempt(attempt)
        assert throttler.get_total_number_of_login_attempts() == 1

    def test_it_can_add_multiple_login_attempts(self):
        throttler = Throttler()
        attempts = [mock_attempt(ip = '88.126.21.23', user_id = 3)] * 5
        throttler.add_login_attempts(attempts)
        assert throttler.get_total_number_of_login_attempts() == 5

    def test_it_finds_the_number_of_login_attempts_by_ip_and_username(self):
        throttler = Throttler()
        attempt = mock_attempt(ip = '88.126.21.23', user_id = 3)
        attempts = [mock_attempt(ip = '88.126.21.23', user_id = 3)] * 10
        throttler.add_login_attempts(attempts)
        assert throttler.get_number_of_similar_attempts_for(attempt) == 10

    def test_it_finds_zero_login_attempts_if_no_login_attempts_have_been_added(self):
        throttler = Throttler()
        attempt = mock_attempt(ip = '88.126.21.23', user_id = 3)
        throttler.add_login_attempts([])
        assert throttler.get_number_of_similar_attempts_for(attempt) == 0
