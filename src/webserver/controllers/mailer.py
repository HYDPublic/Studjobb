from controller import Controller
import datetime
from src.mail.mail import Mail
from src.mail.schedueled_entry import SchedueledEntry
from src.mail.best_send_date import BestSendDate 
from src.database.schedueled_entry_repository import SchedueledEntryRepository
from src.database.job_repository import JobRepository
from src.database.template_repository import TemplateRepository

class MailerController(Controller):
    
    def __init__(self, database):
        self.schedueled_entry_repository = SchedueledEntryRepository(database) 
        self.job_repository = JobRepository(database) 
        self.template_repository = TemplateRepository(database) 
        super(MailerController, self).__init__()

    @Controller.authentication_required
    def new(self, id):
        job = self.job_repository.find(id)
        template_id = self.request.args.get('template')
        if not template_id:
            template_id = 1

        current_template = self.template_repository.find(template_id)
        if not job or not current_template:
            return self.abort(404)

        templates = self.template_repository.findAll()
        current_template.job = job

        return self.render('admin/mail/new.html',
            job                   = job,
            templates             = templates,
            current_template      = current_template,
            reccomended_send_date = BestSendDate()
        ) 

    @Controller.authentication_required
    def create(self, id):
        mail = Mail(
            recipient      = self.request.form['recipient'],
            recipient_name = self.request.form['recipient_name'],
            sender_name    = 'Michael McMillan',
            sender         = 'michael@studjobb.no',
            subject        = self.request.form['subject'],
            body           = self.request.form['body']
        ) 
        
        when = datetime.datetime.strptime(self.request.form['when'], '%Y-%m-%dT%H:%M')
        schedueled_entry = SchedueledEntry(mail, when)
        self.schedueled_entry_repository.create(schedueled_entry)

        return self.redirect(self.url_for('board.control_panel'))
