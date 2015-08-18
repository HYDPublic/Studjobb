# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class DescriptionException(Exception):
    pass

class Description(object):
    validHTMLTags = [
        'h1', 'h2', 'h3', 'h4', 'h5',
        'b', 'i', 'em', 'p', 'img',
        'ul', 'li', 'a', 'strong', 'div',
        'br', 'span', 'form'
    ]

    def __init__(self, text):
        if self.isValid(text):
            self._text = text

    def __str__(self):
        return self._text

    def isValid(self, text):
        illegalHTMLTags = self.hasIllegalHTMLTags(text)
        if illegalHTMLTags:
            raise DescriptionException("Description contains illegal html tags: %s" % ', '.join(str(tag) for tag in illegalHTMLTags))
        elif self.hasTooManyWords(text):
            raise DescriptionException("Description is too long.")
        else:
            return True

    def hasIllegalHTMLTags(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        allHTMLTags = soup.findAll(True)

        illegalHTMLTags = []
        for HTMLTag in allHTMLTags:
            if HTMLTag.name not in Description.validHTMLTags:
                illegalHTMLTags.append(HTMLTag.name) 

        if not illegalHTMLTags:
            return False 
        else:
            return illegalHTMLTags

    def hasTooManyWords(self, text):
        wordCountInDescription = len(text.split())
        return wordCountInDescription >= 1000

