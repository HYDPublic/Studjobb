# -*- coding: utf-8 -*-
import re
import string

class TitleException(Exception):
    pass

class Title(object):
    
    @staticmethod
    def hasInvalidType(title):
        return isinstance(title, basestring) == False
    
    @staticmethod
    def hasInvalidCharacters(title):
        validCharacters = "æøåÆØÅ" + string.printable
        return all(validCharacter in validCharacters for validCharacter in title) == False

    @staticmethod
    def hasTooFewCharacters(title):
        return len(title) <= 5

    @staticmethod
    def hasTooManyCharacters(title):
        return len(title) > 50
        
    @staticmethod
    def hasHTMLTags(title):
        return re.match('<.*?>', title)

    @staticmethod
    def isValid(title):
        if Title.hasInvalidType(title):
            raise TitleException('Title must be a string.')
        if Title.hasTooFewCharacters(Title.format(title)):
            raise TitleException('Title must be longer than 5 characters.')
        elif Title.hasTooManyCharacters(Title.format(title)):
            raise TitleException('Title must be shorther than 50 characters.')
        elif Title.hasHTMLTags(title):
            raise TitleException('Title seems to contain HTML-tags.')
#        elif Title.hasInvalidCharacters(title):
#            raise TitleException('Title must only contain letters, digits and symbols.')
        else:
            return True

    @staticmethod
    def capitalizeFirstLetter(title):
        firstLetterOfTitle = title[0]
        restOfTitle        = title[1:]
        return firstLetterOfTitle.title() + restOfTitle 

    @staticmethod
    def format(title):
        title = Title.capitalizeFirstLetter(title) 

        # Strip whitespace
        title = title.strip()
        
        # Remove linebreaks
        title = title.replace('\n', ' ')

        return title
