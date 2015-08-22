# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.mail.mail import Mail 
from src.mail.schedueler import Schedueler 
from src.mail.schedueled_entry import SchedueledEntry 

class FakeMail(Mail):
    def __init__(self, id = None):
        self.id = id

class TestSchedueler(unittest.TestCase):

    def test_schedueler_can_enqueue_a_single_mail(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(), when = None)
        self.assertEqual(len(schedueler.queue), 1)

    def test_schedueler_can_enqueue_multiple_mails(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(), when = None)
        schedueler.enqueue(mail = FakeMail(), when = None)
        schedueler.enqueue(mail = FakeMail(), when = None)
        self.assertEqual(len(schedueler.queue), 3)

    def test_schedueler_can_remove_duplicate_mails(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(id = 1), when = None)
        schedueler.enqueue(mail = FakeMail(id = 1), when = None)
        schedueler.remove_duplicates()
        self.assertEqual(len(schedueler.queue), 1)

    def test_schedueler_extracts_one_mail_if_its_scheduele_time_is_in_the_past(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(), when = datetime.datetime(2015, 01, 01, 8, 30))
        mock_now = datetime.datetime(2016, 01, 01, 9, 0)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 1)

    def test_schedueler_extracts_no_mail_if_its_scheduele_time_is_in_the_future(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(), when = datetime.datetime(2016, 01, 01, 9, 0))
        mock_now = datetime.datetime(2015, 01, 01, 8, 30)
        self.assertEqual(len(schedueler.mails_to_be_sent_now(now = mock_now)), 0)

    def test_schedueler_clears_sent_jobs_after_run(self):
        schedueler = Schedueler()
        schedueler.enqueue(mail = FakeMail(), when = datetime.datetime(2016, 01, 01,  9, 0))
        schedueler.send(now = datetime.datetime(2018, 01, 01, 8, 30))
        self.assertEqual(len(schedueler.queue), 0)

    def test_schedueler_can_take_schedueler_entries_in_constructor(self):
        schedueler = Schedueler([
            SchedueledEntry(FakeMail(), datetime.datetime(2016, 01, 01)),
            SchedueledEntry(FakeMail(), datetime.datetime(2017, 01, 01)),
            SchedueledEntry(FakeMail(), datetime.datetime(2018, 01, 01))
        ])
        self.assertEqual(len(schedueler.queue), 3)
