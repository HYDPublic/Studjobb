from sqlalchemy.sql  import text
from src.email.email import Email 
from src.email.schedueled_email import SchedueledEmail 

class SchedueledEmailRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'schedueled_emails'

    def find(self, id):
        result = self._database.execute(text(
            """SELECT * FROM :table WHERE id = :id"""
        ), 
            id    = id,
            table = self._table
        )
        row = result.fetchone()
        email = Email(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
        schedueled_email = SchedueledEmail(email = email, when = row.when)
        return email 

    def findAll(self):
        result = self._database.execute(text(
            """SELECT * FROM :table"""
        ),
            table = self._table
        )
        schedueled_emails = []
        for row in result:
            email = Email(id = row.id, recipient = row.recipient, sender = row.sender, subject = row.subject, body = row.body)
            schedueled_email = SchedueledEmail(email = email, when = row.when)
            schedueled_emails.append(schedueled_email)

        return schedueled_emails 

    def save(self, schedueled_email):
        if schedueled_email.id is None:
            return self.create(schedueled_email)
        else:
            return self.update(schedueled_email)

    def update(self, schedueled_email):
        result = self._database.execute(text(
            """UPDATE :table SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body,
            when      = :when
            WHERE id = :id"""
        ),
            recipient = schedueled_email.recipient,
            sender    = schedueled_email.sender,
            subject   = schedueled_email.subject,
            body      = schedueled_email.body,
            when      = schedueled_email.when,
            id        = schedueled_email.id,
            table     = self._table
        )
        return self.find(email.id) 

    def create(self, email):
        result = self._database.execute(text(
            """INSERT INTO :table SET
            recipient = :recipient,
            sender    = :sender,
            subject   = :subject,
            body      = :body"""
        ),
            recipient = email.recipient,
            sender    = email.sender,
            subject   = email.subject,
            body      = email.body,
            table     = self._table
        )
        email.id = result.lastrowid
        return email 
