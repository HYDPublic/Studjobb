from mock import MagicMock 
import unittest
from src.throttler.jail import Jail

# Cell: All prisoners grouped in here.
# Prisoner: Something with an identifier
# ReleasePolicy: The rule that determines if a prisoner should be let free.
def mock_prisoner(ip, user_id):
    prisoner = MagicMock()
    prisoner.user_id = user_id
    prisoner.ip = ip
    prisoner.identifier = (ip, user_id)
    return prisoner

class TestJail(unittest.TestCase):

    def test_it_has_no_prisoners_by_default(self):
        jail = Jail()
        assert jail.get_total_number_of_prisoners() == 0

    def test_it_can_add_a_prisoner(self):
        jail = Jail()
        prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        jail.add_prisoner(prisoner)
        assert jail.get_total_number_of_prisoners() == 1

    def test_it_can_add_multiple_prisoners(self):
        jail = Jail()
        prisoners = [mock_prisoner(ip = '88.126.21.23', user_id = 3)] * 5
        jail.add_prisoners(prisoners)
        assert jail.get_total_number_of_prisoners() == 5

    def test_it_finds_the_number_of_prisoners_by_ip_and_username(self):
        jail = Jail()
        prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        prisoners = [mock_prisoner(ip = '88.126.21.23', user_id = 3)] * 10
        jail.add_prisoners(prisoners)
        assert jail.get_number_of_prisoners_in_same_cell_as(prisoner) == 10

    def test_it_finds_zero_prisoners_if_no_prisoners_have_been_added(self):
        jail = Jail()
        prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        jail.add_prisoners([])
        assert jail.get_number_of_prisoners_in_same_cell_as(prisoner) == 0

    def test_it_can_release_similar_prisoners(self):
        jail = Jail()
        prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        prisoners = [mock_prisoner(ip = '88.126.21.23', user_id = 3)] * 10
        jail.add_prisoners(prisoners)
        jail.release_prisoners_in_same_cell_as(prisoner)
        assert jail.get_number_of_prisoners_in_same_cell_as(prisoner) == 0

    def test_it_does_not_release_different_prisoners(self):
        jail = Jail()
        prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        different_prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 4)
        similar_prisoner = mock_prisoner(ip = '88.126.21.23', user_id = 3)
        jail.add_prisoners([similar_prisoner, different_prisoner])
        jail.release_prisoners_in_same_cell_as(prisoner)
        assert jail.get_total_number_of_prisoners() == 1
