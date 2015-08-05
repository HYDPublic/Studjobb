# -*- coding: utf-8 -*-
class DescriptionException(Exception):
    pass

class Description(object):

    @staticmethod
    def isValid(description):
        if "script" in description:
            raise DescriptionException("lol")
        return True
