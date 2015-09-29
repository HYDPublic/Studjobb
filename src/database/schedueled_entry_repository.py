from sqlalchemy.sql  import text
from src.mail.mail import Mail 
from src.mail.schedueled_entry import SchedueledEntry 

class SchedueledEntryRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'schedueled_entries'

    def find(self, id):
        result = self._database.execute(text(
            """SELECT * FROM %s WHERE id = :id"""
        % self._table), 
            id = id
        )
        row = result.fetchone()
        mail = Mail(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
        return SchedueledEntry(mail = mail, when = row.when, sent = row.sent)

    def findAll(self):
        result = self._database.execute(text(
            """SELECT * FROM %s""" % (self._table)
        ))
        schedueled_entries = []
        for row in result:
            mail = Mail(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
            schedueled_entry = SchedueledEntry(mail = mail, when = row.when, sent = row.sent)
            schedueled_entries.append(schedueled_entry)
        return schedueled_entries 

    def save(self, schedueled_entry):
        if schedueled_entry.id is None:
            return self.create(schedueled_entry)
        else:
            return self.update(schedueled_entry)

    def update(self, schedueled_entry):
        result = self._database.execute(text(
            """UPDATE %s SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body,
            schedueled_entries.when = :when,
            sent      = :sent
            WHERE id  = :id"""
        % self._table),
            id        = schedueled_entry.mail.id,
            recipient = schedueled_entry.mail.recipient,
            sender    = schedueled_entry.mail.sender,
            subject   = schedueled_entry.mail.subject,
            body      = schedueled_entry.mail.body,
            when      = schedueled_entry.when,
            sent      = schedueled_entry.sent
        )
        return self.find(schedueled_entry.mail.id) 

    def create(self, schedueled_entry):
        result = self._database.execute(text(
            """INSERT INTO %s SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            sent      = :sent,
            schedueled_entries.when = :when,
            body      = :body"""
        % self._table),
            recipient = schedueled_entry.mail.recipient,
            sender    = schedueled_entry.mail.sender,
            subject   = schedueled_entry.mail.subject,
            body      = schedueled_entry.mail.body,
            when      = schedueled_entry.when,
            sent      = schedueled_entry.sent 
        )
        schedueled_entry.mail.id = result.lastrowid
        return schedueled_entry 
