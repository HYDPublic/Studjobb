# -*- coding: utf-8 -*-
import unittest 
from src.person.person import Person 

class TestPersonName(unittest.TestCase):

    def test_person_has_first_and_lastname_separated_by_whitespace(self):
        person = Person(firstName = "Michael", lastName = "McMillan")
        self.assertEqual(person.name, "Michael McMillan")

    def test_person_has_no_whitespace_if_only_firstname_is_provided(self):
        person = Person(firstName = "Michael")
        self.assertEqual(person.name, "Michael")

    def test_person_has_no_whitespace_if_only_lastname_is_provided(self):
        person = Person(lastName = "McMillan")
        self.assertEqual(person.name, "McMillan")
