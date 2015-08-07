# -*- coding: utf-8 -*-
import re

class NameException(Exception):
    pass

class Name(object):

    @staticmethod
    def hasHTMLTags(name):
        return re.match('<.*?>', name)
    
    @staticmethod
    def isValid(name):
        if Name.hasHTMLTags(name):
            raise NameException('Name can not contain HTML.')
        return True

    @staticmethod
    def format(name):
        return name.strip()
