import unittest
from mock import MagicMock
from datetime import datetime, timedelta

class Guard(object):

    def imprison(self, prisoner, jail):
        prisoner.imprisoned_at = datetime.now()
        jail.add_prisoner(prisoner)

    def release(self, prisoner, jail):
        jail.release_prisoners_in_same_cell_as(prisoner)

    def find_oldest_prisoner_sharing_cell_with(self, prisoner, jail):
        prisoners_sharing_cell = jail.get_prisoners_in_same_cell_as(prisoner)
        return sorted(prisoners_sharing_cell, key=lambda prisoner: prisoner.imprisoned_at)[0]

class TestGuard(unittest.TestCase):

    def test_guard_can_imprison_a_prisoner(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.imprison(prisoner, jail)
        jail.add_prisoner.assert_called_with(prisoner)

    def test_guard_can_release_a_prisoner(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.release(prisoner, jail)
        jail.release_prisoners_in_same_cell_as.assert_called_with(prisoner)

    def test_guard_sets_an_imprisoned_timestamp_on_prisoner_when_imprisoned(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.imprison(prisoner, jail)
        assert prisoner.imprisoned_at <= datetime.now()

    @unittest.skip('')
    def test_determines_prisoner_should_be_released_when_policy_time_is_served(self):
        guard = Guard()
        prisoner, jail, release_policy = MagicMock(), MagicMock(), MagicMock()
        prisoner.imprisoned_at = datetime(2000, 4, 4)
        release_policy.release_after = timedelta(hours=24)
        assert guard.is_release_due(prisoner, jail, release_policy) == True

    def test_can_find_the_oldest_prisoner_sharing_a_cell_with_prisoner(self):
        guard = Guard()
        old_prisoner, recent_prisoner, jail = MagicMock(), MagicMock(), MagicMock()
        old_prisoner.imprisoned_at = datetime(2010, 1, 1)
        recent_prisoner.imprisoned_at = datetime(2015, 2, 2)
        jail.get_prisoners_in_same_cell_as.return_value = [old_prisoner, recent_prisoner]
        assert guard.find_oldest_prisoner_sharing_cell_with(recent_prisoner, jail) == old_prisoner

#    def test_determines_prisoner_should_not_be_released_when_policy_time_is_not_served(self):
#        guard = Guard()
#        prisoner, jail, release_policy = MagicMock(), MagicMock(), MagicMock()
#        release_policy.release_after = timedelta(hours=24)
#        assert guard.is_release_due(prisoner, jail, release_policy) == False
