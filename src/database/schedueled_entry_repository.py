from sqlalchemy.sql  import text
from src.mail.mail import Mail 
from src.mail.schedueled_entry import SchedueledEntry 

class SchedueledEntryRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'schedueled_entries'

    def find(self, id):
        result = self._database.execute(text(
            """SELECT * FROM :table WHERE id = :id"""
        ), 
            id    = id,
            table = self._table
        )
        row = result.fetchone()
        mail = Mail(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
        return SchedueledEntry(mail = mail, when = row.when)

    def findAll(self):
        result = self._database.execute(text(
            """SELECT * FROM :table"""
        ),
            table = self._table
        )
        schedueled_entries = []
        for row in result:
            mail = Mail(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
            schedueled_entries.append(SchedueledEntry(mail = mail, when = row.when))
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
            recipient = schedueled_entry.mail.recipient,
            sender    = schedueled_entry.mail.sender,
            subject   = schedueled_entry.mail.subject,
            body      = schedueled_entry.mail.body,
            when      = schedueled_entry.mail.when,
            id        = schedueled_entry.mail.id,
            table     = self._table
        )
        return self.find(schedueled_entry.mail.id) 

    def create(self, schedueled_entry):
        result = self._database.execute(text(
            """INSERT INTO %s SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body"""
        % self._table),
            recipient = schedueled_entry.mail.recipient,
            sender    = schedueled_entry.mail.sender,
            subject   = schedueled_entry.mail.subject,
            body      = schedueled_entry.mail.body
        )
        schedueled_entry.mail.id = result.lastrowid
        return schedueled_entry 
