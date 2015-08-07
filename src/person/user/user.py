# -*- coding: utf-8 -*-
from src.person.person import Person

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
