from datetime import datetime

class ReleasePolicy(object):

    @staticmethod
    def should_be_released(prisoner):
        date_now = datetime.now()
        date_for_release = prisoner.imprisoned_at + prisoner.sentence.time
        return date_for_release <= date_now

