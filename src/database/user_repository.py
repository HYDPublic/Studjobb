from src.user.user import User 

class UserRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'users'

    def find(self, email):
        result = self._database.execute('select * from persons join %s on id = person_id where email = "%s"' % (self._table, email))
        row = result.fetchone()
        if row is None:
            return None
        else:
            return User(firstName = row.firstname, lastName = row.lastname, email = row.email, password = row.password)

    def save(self, job):
        pass

    def remove(self, job):
        pass
