class EmailException(Exception):
    pass

class Email(object):

    @staticmethod
    def doesNotContainExactlyOneAtSign(email):
        return (len(email.split('@')) != 2)

    @staticmethod
    def isValid(email):
        if email is None:
            return False
        elif Email.doesNotContainExactlyOneAtSign(email):
            raise EmailException("Invalid email address.")
        return True
