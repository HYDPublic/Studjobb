# -*- coding: utf-8 -*-
from src.mail.mail import Mail

class SchedueledEntry(object):

    def __init__(self, mail, when, sent = False):
        self.mail = mail
        self.when = when 
        self.sent = sent 

    @property
    def id(self):
        return self.mail.id

    def __eq__(self, other_mail_id):
        return self.mail.id == other_mail_id

    def __hash__(self):
        return self.mail.id
