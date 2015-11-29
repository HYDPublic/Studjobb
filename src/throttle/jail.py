class Jail(object):

    def __init__(self):
        self._prisoners = {}

    def prisoner_is_imprisoned(self, prisoner):
        return prisoner in self._prisoners

    def throw_in(self, prisoner):
        if self.prisoner_is_imprisoned(prisoner):
            raise Exception('Prisoner already in jail.')
        self._prisoners[prisoner] = prisoner

    def throw_out(self, prisoner):
        if not self.prisoner_is_imprisoned(prisoner):
            raise Exception('Prisoner not in jail.')
        del self._prisoners[prisoner]

    @property
    def prisoners(self):
        return self._prisoners

    @property
    def number_of_prisoners(self):
        return len(self._prisoners) 
