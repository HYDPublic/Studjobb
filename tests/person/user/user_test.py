# -*- coding: utf-8 -*-
import unittest 
from src.person.user.user import User 
from src.person.user.user import UserException

class TestUser(unittest.TestCase):
    
    def test_user_raises_exception_if_email_is_not_provided(self):
        self.assertRaisesRegexp(UserException, "email", User, password = "h@h")

    def test_user_raises_exception_if_password_is_not_provided(self):
        self.assertRaisesRegexp(UserException, "password", User, email = "h@h")
