from datetime import datetime, timedelta

class Crime(object):
    def __init__(self, victim = None, punishment = None):
        if not victim:
            raise Exception('Missing victim of crime.')
        self.victim = victim
        self._punishment = punishment

    @property
    def punishment(self):
        if self._punishment:
            return max(self._punishment, timedelta(0))
        else:
            return timedelta(0)
