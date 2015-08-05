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
        if Job.isValidTitle(title):
            self._title = Job.formatTitle(title)

    @staticmethod
    def isValidTitle(title):
        # Type must be string
        if isinstance(title, str) == False:
            raise TitleException('Title must be a string.')

        # Title length
        formattedTitle = Job.formatTitle(title)
        if len(title) <= 5:
            raise TitleException('Title must be longer than 5 characters.')
        elif len(title) > 50:
            raise TitleException('Title must be shorter than 50 characters.')

        # HTML tags 
        if re.match('<.*?>', title):
            raise TitleException('Title seems to contain HTML-tags.')
        
        return True 

    @staticmethod
    def formatTitle(title):
        # Capitalize first letter only
        firstLetterOfTitle = title[0]
        restOfTitle        = title[1:]
        title              = firstLetterOfTitle.title() + restOfTitle 

        # Strip whitespace
        title = title.strip()
        
        # Remove linebreaks
        title = title.replace('\n', ' ')

        return title
