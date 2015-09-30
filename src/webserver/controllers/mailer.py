from controller import Controller
import datetime
from src.mail.mail import Mail
from src.mail.schedueled_entry import SchedueledEntry
from src.database.schedueled_entry_repository import SchedueledEntryRepository

class MailerController(Controller):
    
    def __init__(self, database):
        self.schedueled_entry_repository = SchedueledEntryRepository(database) 
        super(MailerController, self).__init__()

    def create(self, id):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        mail = Mail(
            recipient = self.request.form['recipient'],
            # This must not be a constant
            sender    = 'michael@studjobb.no',
            subject   = self.request.form['subject'],
            body      = self.request.form['body']
        ) 
        
        when = datetime.datetime.strptime(self.request.form['when'], '%Y-%m-%dT%H:%M')
        schedueled_entry = SchedueledEntry(mail, when)
        self.schedueled_entry_repository.create(schedueled_entry)

        return self.redirect(self.url_for('board.control_panel'))
