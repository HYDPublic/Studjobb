import re

class TitleException(Exception):
    pass

class Job(object):

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        formattedTitle = Job.formatTitle(title)
        if Job.isValidTitle(formattedTitle):
            self._title = formattedTitle

    @staticmethod
    def isValidTitle(title):

        # Title length
        lengthOfTitle = len(title)
        if lengthOfTitle <= 5:
            raise TitleException('Title must be longer than 5 characters.')
        elif lengthOfTitle > 50:
            raise TitleException('Title must be shorter than 50 characters.')
        # HTML tags 
        elif re.match('<.*?>', title):
            raise TitleException('Title seems to contain HTML-tags.')
        else:
            return True

    @staticmethod
    def formatTitle(title):
        firstLetterOfTitle = title[0]
        restOfTitle        = title[1:]
        titleCapitalized   = firstLetterOfTitle.title() + restOfTitle 

        return titleCapitalized \
            .strip()            \
            .replace('\n', ' ')
