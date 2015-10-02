import datetime

class BestSendDate(object):

    weekdays = [
        'monday',   'tuesday', 'wednesday',
        'thursday', 'friday',  'saturday',
        'sunday'
    ]

    def __init__(self, now = False):
        self._now              = now or datetime.datetime.now() 
        self._hour_threshold   = 14

        self._preferred_hour   = 10
        self._preferred_minute = 45

    def adjust_time_of_day_preferred(self, date):
        return date.replace(hour=self._preferred_hour, minute=self._preferred_minute)

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
    
    def current_date_is_past_hour_threshold(self):
        return self._now.hour > self._hour_threshold 

    def tomorrows_date(self):
        return self._now + datetime.timedelta(1)

    def next_monday(self):
        return self.next_date_for_weekday(self._now, 'monday')

    def todays_date(self):
        return self._now

    @property
    def date(self):
        if self.current_date_is_in_weekend():
            return self.adjust_time_of_day_preferred(self.next_monday())

        elif self.current_date_is_past_hour_threshold():
            if self.current_date_is_friday():
                return self.adjust_time_of_day_preferred(self.next_monday())            
            else:
                return self.adjust_time_of_day_preferred(self.tomorrows_date())

        else:
            return self.todays_date()
