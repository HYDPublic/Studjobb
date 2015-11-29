import unittest
from mock import MagicMock
from src.throttle.jail import Jail

class TestJail(unittest.TestCase):

    def test_it_has_no_prisoners_by_default(self):
        jail = Jail()
        assert jail.number_of_prisoners == 0

    def test_prisoner_can_be_added_to_jail(self):
        jail = Jail()
        prisoner = MagicMock()
        jail.throw_in(prisoner)
        assert jail.number_of_prisoners == 1
    
    def test_prisoner_can_not_be_added_twice(self):
        jail = Jail()
        prisoner = MagicMock()
        jail.throw_in(prisoner)
        with self.assertRaisesRegexp(Exception, 'already in jail'):
            jail.throw_in(prisoner)

    def test_prisoner_can_be_removed_from_jail(self):
        jail = Jail()
        prisoner = MagicMock()
        jail.throw_in(prisoner)
        jail.throw_out(prisoner)
        assert jail.number_of_prisoners == 0

    def test_prisoner_not_in_jail_can_not_be_removed_from_jail(self):
        jail = Jail()
        prisoner_not_in_jail = MagicMock()
        with self.assertRaisesRegexp(Exception, 'not in jail'):
            jail.throw_out(prisoner_not_in_jail)
