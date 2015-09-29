class MailAddressException(Exception):
    pass

class MailAddress(object):

    @staticmethod
    def doesNotContainExactlyOneAtSign(email):
        return (len(email.split('@')) != 2)

    @staticmethod
    def isValid(email):
        if email is None:
            return False
        elif MailAddress.doesNotContainExactlyOneAtSign(email):
            raise MailAddressException("Invalid email address.")
        return True
