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
        title = title[0].title() + title[1:] 
        return title \
            .strip() \
            .replace('\n', ' ')
