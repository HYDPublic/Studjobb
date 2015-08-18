# -*- coding: utf-8 -*-
import re
import string

class TitleException(Exception):
    pass

class Title(object):
    
    def __init__(self, text = 'Mangler tittel'):
        if self.isValid(text):
            self._text = self.format(text)

    def __str__(self):
        return self._text

    def format(self, title):
        return self.capitalizeFirstLetter(title).strip().replace('\n', ' ')

    def isValid(self, text):
        if self.hasInvalidType(text):
            raise TitleException('Title must be a string.')
        elif self.hasTooFewCharacters(self.format(text)):
            raise TitleException('Title must be longer than 5 characters.')
        elif self.hasTooManyCharacters(self.format(text)):
            raise TitleException('Title must be shorther than 50 characters.')
        elif self.hasHTMLTags(text):
            raise TitleException('Title seems to contain HTML-tags.')
        else:
            return True

    def hasInvalidType(self, title):
        return isinstance(title, basestring) == False
    
    def hasInvalidCharacters(self, title):
        validCharacters = "æøåÆØÅ" + string.printable
        return all(validCharacter in validCharacters for validCharacter in title) == False

    def hasTooFewCharacters(self, title):
        return len(title) <= 5

    def hasTooManyCharacters(self, title):
        return len(title) > 50
        
    def hasHTMLTags(self, title):
        return re.match('<.*?>', title)

    def capitalizeFirstLetter(self, title):
        firstLetterOfTitle = title[0]
        restOfTitle        = title[1:]
        return firstLetterOfTitle.title() + restOfTitle 
