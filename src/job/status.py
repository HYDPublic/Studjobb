# -*- coding: utf-8 -*-
class StatusException(Exception):
    pass

class Status(object):
    
    codes = ['active', 'pending', 'dead']

    def __init__(self, code = None):
        code = code or 'pending'
        code = code.lower()
        if self.isValid(code):
            self._code = code

    def __str__(self):
        return self._code

    def isValid(self, code):
        if code not in Status.codes:
            raise StatusException('Invalid status code')
        else:
            return True
