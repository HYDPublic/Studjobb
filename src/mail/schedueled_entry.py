# -*- coding: utf-8 -*-
from src.mail.mail import Mail

class SchedueledEntry(object):

    def __init__(self, mail, when):
        self.mail = mail
        self.when  = when 

    def __eq__(self, other_id):
        return self.mail.id == other_id

    def __hash__(self):
        return self.mail.id
