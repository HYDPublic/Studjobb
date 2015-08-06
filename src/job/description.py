# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class DescriptionException(Exception):
    pass

class Description(object):
    validHTMLTags = [
        'h1', 'h2', 'h3', 'h4', 'h5',
        'b', 'i', 'em', 'p', 'img',
        'ul', 'li', 'a', 'strong'
    ]

    @staticmethod
    def hasIllegalHTMLTags(description):
        soup = BeautifulSoup(description, 'html.parser')
        allHTMLTags = soup.findAll(True)

        for HTMLTag in allHTMLTags:
            if HTMLTag.name not in Description.validHTMLTags:
                return True
        return False

    @staticmethod
    def hasTooManyWords(description):
        wordCountInDescription = len(description.split())
        return wordCountInDescription >= 1000

    @staticmethod
    def isValid(description):
        if Description.hasIllegalHTMLTags(description):
            raise DescriptionException("Description contains illegal html tags.")
        elif Description.hasTooManyWords(description):
            raise DescriptionException("Description is too long.")
        return True
