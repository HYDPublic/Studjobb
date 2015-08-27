import base64
from src.database.engine import database
from src.database.user_repository import UserRepository

class AuthenticationException(Exception):
    pass

class Authentication():
    
    def __init__(self):
        self.user_repository = UserRepository(database) 

    def decode_credentials(self, credentials):
        return base64.b64decode(credentials)

    def contains_exactly_one_character(self, string, character):
        return string.count(character) == 1

    def contains_username_and_password(self, string):
        return string.index(':') != 0 and string.index(':') != len(string) - 1

    def extract_encoded_credentials(self, string):
        return string.replace('Basic ', '', 1)

    def split_credentials(self, string):
        parts = string.split(':')
        return {
            'username': parts[0],
            'password': parts[1]
        }

    def authenticate_response_header(self):
        return 'Basic realm="Authentication Required"'

    def is_prefixed_with_basic(self, authentication_header):
        return authentication_header[:6] == 'Basic '

    def is_valid_authentication_format(self, authentication_header):

        if not authentication_header:
            return False
        elif self.is_prefixed_with_basic(authentication_header) == False:
            return False
        elif self.contains_exactly_one_character(authentication_header, ' ') == False:
            return False

        encoded_credentials = self.extract_encoded_credentials(authentication_header)
        decoded_credentials = self.decode_credentials(encoded_credentials)

        if self.contains_exactly_one_character(decoded_credentials, ':') == False:
            return False
        elif self.contains_username_and_password(decoded_credentials) == False:
            return False
        
        return True

    def look_up_user(self, username):
        user = self.user_repository.find(username)
        if user is None:
            raise AuthenticationException('User not found.') 
        else:
            return user

    def verify_credentials(self, username, password):
        user = self.look_up_user(username)
        return user.checkCredentials(password)
