# -*- coding: utf-8 -*-
import mock
import unittest 
import datetime
import smtplib
from src.mail.mail import Mail 
from src.mail.schedueler import Schedueler 
from src.mail.schedueled_entry import SchedueledEntry 

class FakeMail(Mail):
    def __init__(self, id = None):
        self.id = id

class TestSchedueler(unittest.TestCase):

    def test_schedueled_entry_is_not_sent_by_default(self):
        schedueled_entry = SchedueledEntry(FakeMail(), datetime.datetime(2016, 01, 01))
        self.assertEqual(schedueled_entry.sent, False);

    def test_schedueler_extracts_one_mail_if_its_scheduele_time_is_in_the_past(self):
        schedueled_entries = [SchedueledEntry(mail = FakeMail(), when = datetime.datetime(2015, 01, 01, 8, 30))]
        schedueler = Schedueler(schedueled_entries)
        mock_now = datetime.datetime(2016, 01, 01, 9, 0)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 1)

    def test_schedueler_extracts_no_mail_if_its_scheduele_time_is_in_the_future(self):
        schedueled_entries = [SchedueledEntry(mail = FakeMail(), when = datetime.datetime(2016, 01, 01, 8, 30))]
        schedueler = Schedueler(schedueled_entries)
        mock_now = datetime.datetime(2015, 01, 01, 8, 30)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 0)

    def test_schedueler_extracts_no_mail_if_its_already_marked_as_sent(self):
        past = datetime.datetime(2000, 01, 01, 12, 0)
        schedueler = Schedueler([SchedueledEntry(mail = FakeMail(), sent = True, when = past)])
        mock_now = datetime.datetime(2015, 01, 01, 8, 30)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 0)

    def test_schedueler_extracts_mail_if_its_not_marked_as_sent(self):
        past = datetime.datetime(2000, 01, 01, 12, 0)
        schedueler = Schedueler([SchedueledEntry(mail = FakeMail(), sent = False, when = past)])
        mock_now = datetime.datetime(2015, 01, 01, 8, 30)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 1)

    @mock.patch('src.mail.mailer.Mailer.send')
    def test_schedueler_clears_sent_jobs_after_run(self, mock_mailer):
        schedueled_entries = [SchedueledEntry(mail = FakeMail(), when = datetime.datetime(2016, 01, 01,  9, 0))]
        schedueler = Schedueler(schedueled_entries)
        schedueler.run(now = datetime.datetime(2018, 01, 01, 8, 30))
        self.assertEqual(len(schedueler.queue), 0)

    @mock.patch('src.mail.mailer.Mailer.send')
    def test_schedueler_does_not_clear_jobs_if_sender_raises_exception(self, mock_sender):
        mock_sender.side_effect = smtplib.SMTPException('Mail could not be sent.')
        schedueled_entries = [SchedueledEntry(mail = FakeMail(), when = datetime.datetime(2016, 01, 01,  9, 0))]
        schedueler = Schedueler(schedueled_entries)
        schedueler.run(now = datetime.datetime(2018, 01, 01, 8, 30))
        self.assertEqual(len(schedueler.queue), 1)

    def test_schedueler_can_take_schedueler_entries_in_constructor(self):
        schedueler = Schedueler([
            SchedueledEntry(FakeMail(), datetime.datetime(2016, 01, 01)),
            SchedueledEntry(FakeMail(), datetime.datetime(2017, 01, 01)),
            SchedueledEntry(FakeMail(), datetime.datetime(2018, 01, 01))
        ])
        self.assertEqual(len(schedueler.queue), 3)
