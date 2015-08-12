# -*- coding: utf-8 -*-
import unittest 
import mock

from src.user.user import User 
from src.user.user import UserException

class TestUser(unittest.TestCase):
    
    def test_user_raises_exception_if_email_is_not_provided(self):
        self.assertRaisesRegexp(UserException, "email", User, password = "h@h")

    def test_user_raises_exception_if_password_is_not_provided(self):
        self.assertRaisesRegexp(UserException, "password", User, email = "h@h")

    @mock.patch("src.user.user.bcrypt")
    def test_user_credentials_are_valid_if_correct_password_is_supplied(self, mock_bcrypt):
        hashed_password = '$2a$10$WvvTPHKwdBJ3uk0Z37EMR.hLA2W6N9AEBhEgrAOljy2Ae5MtaSIUi'
        mock_bcrypt.hashpw.return_value = hashed_password
        user = User(email = "email@email.com", password = hashed_password)
        valid_credentials = user.checkCredentials(plain_text_password = "abc")
        self.assertEqual(valid_credentials, True)

    @mock.patch("src.user.user.bcrypt")
    def test_user_credentials_are_invalid_if_incorrect_password_is_supplied(self, mock_bcrypt):
        hashed_password = '$2a$10$WvvTPHKwdBJ3uk0Z37EMR.hLA2W6N9AEBhEgrAOljy2Ae5MtaSIUi'
        mock_bcrypt.hashpw.return_value = "not-the-same-hash"
        user = User(email = "email@email.com", password = hashed_password)
        valid_credentials = user.checkCredentials(plain_text_password = "abc")
        self.assertEqual(valid_credentials, False)
