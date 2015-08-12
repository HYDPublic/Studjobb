# -*- coding: utf-8 -*-
from src.person.person import Person
import bcrypt

class UserException(Exception):
    pass

class User(Person):

    def __init__(self, *args, **kwargs):
        if 'password' not in kwargs:
            raise UserException("Users must have password.")
        else:
            self.password = kwargs.pop('password') 

        # Extend Person class
        super(User, self).__init__(*args, **kwargs)

        if self.email is None:
            raise UserException("Users must have email.")

    def checkCredentials(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password, self.password) == self.password

    @staticmethod
    def hashPassword(clear_text_password):
        return bcrypt.hashpw(clear_text_password, bcrypt.gensalt(10))
