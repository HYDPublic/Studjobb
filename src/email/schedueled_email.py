# -*- coding: utf-8 -*-
from src.email.email import Email

class SchedueledEmail(Email):

    def __init__(self, email, when):
        self.when = when 
        super(SchedueledEmail, self).__init__(
            id = email.id,
            recipient = email.recipient,
            sender    = email.sender,
            subject   = email.subject,
            body      = email.body
        )
