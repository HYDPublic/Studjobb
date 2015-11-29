from datetime import datetime
from release_policy import ReleasePolicy

class Guard(object):

    def imprison(self, prisoner, jail):
        prisoner.imprisoned_at = datetime.now()
        jail.throw_in(prisoner)

    def release(self, prisoner, jail):
        jail.throw_out(prisoner)
        prisoner.imprisoned_at = None

    def prisoners_to_be_released(self, jail):
        return [prisoner for prisoner in jail.prisoners \
               if ReleasePolicy.should_be_released(prisoner)]

    def release_prisoners_that_has_served_their_punishment(self, jail):
        prisoners = self.prisoners_to_be_released(jail)
        for prisoner in prisoners:
            self.release(prisoner, jail)
