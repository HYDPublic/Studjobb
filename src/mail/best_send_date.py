import datetime

class BestSendDate(object):

    weekdays = [
        'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday',
        'sunday'
    ]

    def __init__(self, now = datetime.datetime.now()):
        self._now              = now
        self._hour_threshold   = 14
        self._preferred_hour   = 10
        self._preferred_minute = 45

    @staticmethod
    def date_is_in_weekend(date):
        return date.weekday() > 4 

    @staticmethod
    def next_date_for_weekday(since, weekday):
        next_date      = since 
        weekday_number = BestSendDate.weekdays.index(weekday.lower())

        while next_date.weekday() != weekday_number:
            next_date += datetime.timedelta(1)
        return next_date

    def current_date_is_in_weekend(self):
        return self.date_is_in_weekend(self._now) 

    def current_date_is_friday(self):
        return BestSendDate.weekdays[self._now.weekday()] == 'friday' 

    def tomorrows_date(self):
        return self._now + datetime.timedelta(1)
    
    def current_date_is_past_hour_threshold(self):
        return self._now.hour > self._hour_threshold 

    def next_monday(self):
        return self.next_date_for_weekday(self._now, 'monday')

    def todays_date(self):
        return self._now

    @property
    def date(self):
        if self.current_date_is_in_weekend():
            return self.next_monday().replace(hour=self._preferred_hour, minute=self._preferred_minute)

        elif self.current_date_is_past_hour_threshold():
            if self.current_date_is_friday():
                return self.next_monday().replace(hour=self._preferred_hour, minute=self._preferred_minute)
            else:
                return self.tomorrows_date().replace(hour=self._preferred_hour, minute=self._preferred_minute)

        else:
            return self.todays_date()
