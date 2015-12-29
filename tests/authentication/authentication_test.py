# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.webserver.authentication import Authentication 
from src.webserver.authentication import AuthenticationException 

class TestAuthentication(unittest.TestCase):

    def test_authentication_controller_can_extract_encoded_credentials(self):
        authentication_controller = Authentication()
        header_value = 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
        encoded_credentials = authentication_controller.extract_encoded_credentials(header_value)
        self.assertEqual(encoded_credentials, "dXNlcm5hbWU6cGFzc3dvcmQ=")

    def test_authentication_controller_can_extract_encoded_credentials_when_basic_is_part_of_encoded_credentials(self):
        authentication_controller = Authentication()
        header_value = 'Basic dXNlcm5hBasicbWU6cGFzc3dvcmQ='
        encoded_credentials = authentication_controller.extract_encoded_credentials(header_value)
        self.assertEqual(encoded_credentials, "dXNlcm5hBasicbWU6cGFzc3dvcmQ=")

    def test_authentication_controller_can_decode_base64_string(self):
        authentication_controller = Authentication()
        encoded = 'dXNlcm5hbWU6cGFzc3dvcmQ='
        decoded = authentication_controller.decode_credentials(encoded)
        self.assertEqual(decoded, "username:password")

    def test_authentication_controller_can_decode_scandinavian_encoded_base64_string(self):
        authentication_controller = Authentication()
        encoded = 'w6XDpcOlw6XDpTrDpsOmw7jDpcOlw6U='
        decoded = authentication_controller.decode_credentials(encoded)
        self.assertEqual(decoded, "ååååå:ææøååå")

    def test_authentication_controller_returns_false_if_authorization_value_is_not_prefixed_with_basic(self):
        authentication_controller = Authentication()
        header_value = 'Advanced dmFsaWQ6Y3JlZGVudGlhbA==' # valid:credential 
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_contains_spaces_in_encoded_credentials(self):
        authentication_controller = Authentication()
        header_value = 'Basic dmFsaWQ6Y3 JlZGVudGlhbA==' # valid:credential (with space)
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_is_none(self):
        authentication_controller = Authentication()
        header_value = None
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_is_missing_colon(self):
        authentication_controller = Authentication()
        header_value = 'Basic bWlzc2luZztjb2xvbg==' # missing;colon
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_has_multiple_colons(self):
        authentication_controller = Authentication()
        header_value = 'Basic dG9vLW1hbnk6OmNvbG9ucw==' # too-many::colons
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_is_missing_username(self):
        authentication_controller = Authentication()
        header_value = 'Basic OnBhc3N3b3Jk' # :password
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_false_if_authorization_value_is_missing_password(self):
        authentication_controller = Authentication()
        header_value = 'Basic dXNlcm5hbWU6' # username:
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), False)

    def test_authentication_controller_returns_true_if_authorization_value_has_one_colon(self):
        authentication_controller = Authentication()
        header_value = 'Basic dmFsaWQ6Y3JlZGVudGlhbA==' # valid:credential
        self.assertEqual(authentication_controller.is_valid_authentication_format(header_value), True)

    def test_authentication_controller_can_extract_username_and_password(self):
        authentication_controller = Authentication()
        self.assertEqual(authentication_controller.split_credentials('bob:secret123'), { 'username': 'bob', 'password': 'secret123' })

    def test_authentication_controller_can_return_a_header_to_the_client(self):
        authentication_controller = Authentication()
        self.assertEqual(authentication_controller.authenticate_response_header(), 'Basic realm="Authentication Required"')

    @mock.patch('src.webserver.authentication.UserRepository.find')
    def test_authentication_controller_delegates_to_user_repository(self, mock_user_repository):
        authentication_controller = Authentication()
        authentication_controller.look_up_user('bob@example.com')
        mock_user_repository.assert_called_with('bob@example.com')

    @mock.patch('src.webserver.authentication.UserRepository.find')
    def test_authentication_controller_raises_exception_if_user_does_not_exist(self, mock_user_repository):
        with self.assertRaises(AuthenticationException):
            authentication_controller = Authentication()
            mock_user_repository.return_value = None
            authentication_controller.look_up_user('not_a_user@example.com')

    @mock.patch('src.webserver.authentication.UserRepository.find')
    def test_authentication_controller_returns_user_from_lookup(self, mock_user_repository):
        authentication_controller = Authentication()
        mock_user = MagicMock()
        mock_user_repository.return_value = mock_user 
        self.assertEqual(authentication_controller.look_up_user('user@example.com'), mock_user)

    @mock.patch('src.webserver.authentication.Authentication.look_up_user')
    def test_authentication_controller_can_verify_credentials_of_user(self, mock_look_up_user):
        authentication_controller = Authentication()
        mock_user = MagicMock()
        mock_user.checkCredentials.return_value = True
        mock_look_up_user.return_value = mock_user 
        self.assertEqual(authentication_controller.verify_credentials('user@example.com', 'password123'), True)
