from src.person.email import Email

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
        if Email.isValid(email):
            self._email = email
        else:
            self._email = None
