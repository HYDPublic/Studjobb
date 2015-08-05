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

        if len(formattedTitle) <= 5:
            raise TitleException('Title must be longer than 5 characters.')
        elif len(formattedTitle) > 50:
            raise TitleException('Title must be shorter than 50 characters.')

        self._title = formattedTitle

    @staticmethod
    def formatTitle(title):
        firstLetterOfTitle = title[0]
        restOfTitle        = title[1:]
        titleCapitalized   = firstLetterOfTitle.title() + restOfTitle 

        return titleCapitalized \
            .strip()            \
            .replace('\n', ' ')
