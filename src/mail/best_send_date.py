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

    def adjust_date_to_preferred_time(self, date):
        return date.replace(hour=self._preferred_hour, minute=self._preferred_minute)

    @staticmethod
    def date_is_in_weekend(date):
        return date.weekday() > 4 

    @staticmethod
    def is_date_a(date, weekday_name):
        weekday_number = BestSendDate.weekdays.index(weekday_name.lower())
        return date.weekday() == weekday_number

    @staticmethod
    def when_is_the_next_weekday(since, weekday_name):
        while not BestSendDate.is_date_a(since, weekday_name):
            since += datetime.timedelta(1)
        return since 

    def current_date_is_in_weekend(self):
        return self.date_is_in_weekend(self._now) 

    def current_date_is_friday(self):
        return BestSendDate.weekdays[self._now.weekday()] == 'friday' 
    
    def current_date_is_past_hour_threshold(self):
        return self._now.hour > self._hour_threshold 

    def tomorrows_date(self):
        return self._now + datetime.timedelta(1)

    def next_monday(self):
        return self.when_is_the_next_weekday(self._now, 'monday')

    def todays_date(self):
        return self._now

    # Returns optimal_date and True if time needs adjustment
    def find_optimal_date(self):
        if self.current_date_is_in_weekend():
            return (self.next_monday(), True)

        elif self.current_date_is_past_hour_threshold():
            if self.current_date_is_friday():
                return (self.next_monday(), True)
            else:
                return (self.tomorrows_date(), True)
        else:
            return (self.todays_date(), False)

    @property
    def date(self):
        optimal_date, time_must_be_adjusted = self.find_optimal_date()
        if time_must_be_adjusted:
            return self.adjust_date_to_preferred_time(optimal_date)
        return optimal_date

