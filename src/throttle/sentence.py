from datetime import datetime, timedelta

class Sentence(object):
    def __init__(self):
        self.crimes = []

    @property
    def time(self):
        time = timedelta(0)
        for crime in self.crimes:
            time += crime.punishment
        return time

    def add_crime(self, crime):
        self.crimes.append(crime)
