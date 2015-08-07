class EmailException(Exception):
    pass

class Person(object):

    def __init__(self, firstName = "", lastName = "", email = None):
        self._firstName = firstName
        self._lastName  = lastName
        self.email      = email

    @property
    def name(self):
        return (self._firstName + " " + self._lastName).strip()

    @property
    def email(self):
        return self._email 

    @email.setter
    def email(self, email):
        if (email is not None) and ('@' not in email):
            raise EmailException("Invalid email address.")
        self._email = email
