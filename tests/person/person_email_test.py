# -*- coding: utf-8 -*-
import unittest 
from src.user.person import Person 
from src.user.email import EmailException 

class TestPersonEmail(unittest.TestCase):

    def test_person_email_can_be_set(self):
        person = Person(email = "email@email.com")
        self.assertEqual(person.email, "email@email.com")

    def test_person_raises_exception_if_email_does_not_contain_at_char(self):
        self.assertRaisesRegexp(EmailException, "email", Person, email = "email(at)email.com")

    def test_person_does_not_raise_exception_if_email_contain_at_char(self):
        Person(email = "@")

    def test_person_raises_exception_if_email_contains_multiple_at_chars(self):
        self.assertRaisesRegexp(EmailException, "email", Person, email = "email@@email.com")

    def test_person_raises_exception_even_if_email_starts_with_multiple_at_chars(self):
        self.assertRaisesRegexp(EmailException, "email", Person, email = "@email@email.com")

    def test_person_raises_exception_even_email_is_an_empty_string(self):
        self.assertRaisesRegexp(EmailException, "email", Person, email = "")
