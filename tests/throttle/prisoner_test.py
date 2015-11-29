import unittest
from src.throttle.prisoner import Prisoner

class TestPrisoner(unittest.TestCase):

    def test_raises_error_if_invalid_ip_provided(self):
         with self.assertRaisesRegexp(Exception, 'IP'):
             prisoner = Prisoner(ip = '86.256.24.56', user_id = 1)

    def test_error_is_not_raised_if_valid_ip_provided(self):
        prisoner = Prisoner(ip = '86.122.24.56', user_id = 1)
        assert prisoner.ip == '86.122.24.56'

    def test_hash_is_a_tuple_of_ip_and_user_id(self):
        prisoner = Prisoner(ip = '86.122.24.56', user_id = 1)
        assert prisoner.__hash__ == ('86.122.24.56', 1)
    
    def test_no_sentence_by_default(self):
        prisoner = Prisoner(ip = '86.122.24.56', user_id = 1)
        assert prisoner.sentence == None
