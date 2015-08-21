from sqlalchemy.sql  import text
from src.email.email import Email 
from src.email.schedueled_entry import SchedueledEntry 

class SchedueledEntryRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'schedueled_entrys'

    def find(self, id):
        result = self._database.execute(text(
            """SELECT * FROM :table WHERE id = :id"""
        ), 
            id    = id,
            table = self._table
        )
        row = result.fetchone()
        email = Email(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
        return SchedueledEntry(email = email, when = row.when)

    def findAll(self):
        result = self._database.execute(text(
            """SELECT * FROM :table"""
        ),
            table = self._table
        )
        schedueled_entries = []
        for row in result:
            email = Email(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
            schedueled_entries.append(SchedueledEntry(email = email, when = row.when))
        return schedueled_entries 

    def save(self, schedueled_entry):
        if schedueled_entry.id is None:
            return self.create(schedueled_entry)
        else:
            return self.update(schedueled_entry)

    def update(self, schedueled_entry):
        result = self._database.execute(text(
            """UPDATE :table SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body,
            when      = :when
            WHERE id = :id"""
        ),
            recipient = schedueled_entry.email.recipient,
            sender    = schedueled_entry.email.sender,
            subject   = schedueled_entry.email.subject,
            body      = schedueled_entry.email.body,
            when      = schedueled_entry.email.when,
            id        = schedueled_entry.email.id,
            table     = self._table
        )
        return self.find(email.id) 

    def create(self, schedueled_entry):
        result = self._database.execute(text(
            """INSERT INTO :table SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body"""
        ),
            recipient = schedueled_entry.email.recipient,
            sender    = schedueled_entry.email.sender,
            subject   = schedueled_entry.email.subject,
            body      = schedueled_entry.email.body,
            table     = self._table
        )
        email.id = result.lastrowid
        return email 
