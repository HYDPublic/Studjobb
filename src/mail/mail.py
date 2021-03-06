# -*- coding: utf-8 -*-
class MailError(Exception):
    pass

class Mail(object):

    def __init__(self, id = None, recipient = None, recipient_name = None, sender = None, sender_name = None, subject = 'Missing subject', body = None):
        self.id             = id 
        self.recipient      = recipient 
        self.recipient_name = recipient_name
        self.sender         = sender 
        self.sender_name    = sender_name
        self.subject        = subject
        self.body           = body

        self.validate_fields()

    def validate_fields(self):
        if not self.recipient:
            raise MailError('Missing recipient.')

        if not self.sender:
            raise MailError('Missing sender.')

        if not self.body:
            raise MailError('Missing body.')

    def __eq__(self, other_id):
        return self.id == other_id

    def __hash__(self):
        return self.id
