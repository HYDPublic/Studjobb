# -*- coding: utf-8 -*-
class EmailError(Exception):
    pass

class Email(object):

    def __init__(self, recipient = None, sender = None, subject = 'Missing subject', body = None):
        self.recipient = recipient 
        self.sender    = sender 
        self.subject   = subject
        self.body      = body

        self.validate_fields()

    def validate_fields(self):
        if not self.recipient:
            raise EmailError('Missing recipient.')

        if not self.sender:
            raise EmailError('Missing sender.')

        if not self.body:
            raise EmailError('Missing body.')
