# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class DescriptionException(Exception):
    pass

class Description(object):
    validHTMLTags = [
        'h1', 'h2', 'h3', 'h4', 'h5',
        'b', 'i', 'em', 'p', 'img',
        'ul', 'li', 'a', 'strong', 'div'
    ]

    @staticmethod
    def hasIllegalHTMLTags(description):
        soup = BeautifulSoup(description, 'html.parser')
        allHTMLTags = soup.findAll(True)

        illegalHTMLTags = []
        for HTMLTag in allHTMLTags:
            if HTMLTag.name not in Description.validHTMLTags:
                illegalHTMLTags.append(HTMLTag.name) 

        if not illegalHTMLTags:
            return False 
        else:
            return illegalHTMLTags

    @staticmethod
    def hasTooManyWords(description):
        wordCountInDescription = len(description.split())
        return wordCountInDescription >= 1000

    @staticmethod
    def isValid(description):
        illegalHTMLTags = Description.hasIllegalHTMLTags(description)
        if illegalHTMLTags:
            raise DescriptionException("Description contains illegal html tags: %s" % ', '.join(str(tag) for tag in illegalHTMLTags))
        elif Description.hasTooManyWords(description):
            raise DescriptionException("Description is too long.")
        return True
