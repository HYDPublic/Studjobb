import unittest
from mock import MagicMock
from datetime import datetime, timedelta
from src.throttle.guard import Guard

class TestGuard(unittest.TestCase):

    def test_adds_an_imprisonment_timestamp_to_prisoners(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.imprison(prisoner, jail)
        assert prisoner.imprisoned_at <= datetime.now()

    def test_removes_the_imprisonment_timestamp_to_prisoners_upon_release(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.release(prisoner, jail)
        assert prisoner.imprisoned_at == None 

    def test_prisoner_is_thrown_in_jail_when_guard_imprisons(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.imprison(prisoner, jail)
        jail.throw_in.assert_called_with(prisoner)

    def test_prisoner_is_added_to_jail_when_guard_releases(self):
        guard = Guard()
        jail = MagicMock()
        prisoner = MagicMock()
        guard.release(prisoner, jail)
        jail.throw_out.assert_called_with(prisoner)

    def test_it_finds_prisoner_that_has_served_their_sentence(self):
        guard = Guard()
        jail, prisoner = MagicMock(), MagicMock()
        jail.prisoners = [prisoner]
        prisoner.imprisoned_at = datetime.now() - timedelta(hours = 6)
        prisoner.sentence.time = timedelta(hours = 5)
        assert guard.prisoners_to_be_released(jail) == [prisoner]

    def test_it_does_not_return_prisoner_that_has_not_served_their_sentence(self):
        guard = Guard()
        jail, prisoner = MagicMock(), MagicMock()
        jail.prisoners = [prisoner]
        prisoner.imprisoned_at = datetime.now() - timedelta(hours = 5)
        prisoner.sentence.time = timedelta(hours = 6)
        assert guard.prisoners_to_be_released(jail) == []

    def test_it_can_release_prisoners_that_have_served_their_punishment(self):
        guard = Guard()
        guard.release, jail, prisoner = MagicMock(), MagicMock(), MagicMock()
        guard.prisoners_to_be_released = MagicMock(return_value = [prisoner])
        guard.release_prisoners_that_has_served_their_punishment(jail)
        guard.release.assert_called_with(prisoner, jail)
