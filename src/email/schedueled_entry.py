# -*- coding: utf-8 -*-
from src.email.email import Email

class SchedueledEntry(object):

    def __init__(self, email, when):
        self.email = email
        self.when  = when 

    def __eq__(self, other_id):
        return self.email.id == other_id

    def __hash__(self):
        return self.email.id
