# -*- coding: utf-8 -*-
import unittest 
from src.mail.mail import Mail 
from src.mail.mail import MailError

class TestMail(unittest.TestCase):

    def test_mail_needs_recipient(self):
        with self.assertRaisesRegexp(MailError, 'recipient'):
            Mail(recipient = None, sender = True, body = True)

    def test_mail_needs_sender(self):
        with self.assertRaisesRegexp(MailError, 'sender'):
            Mail(recipient = True, sender = None, body = True)

    def test_mail_needs_a_body(self):
        with self.assertRaisesRegexp(MailError, 'body'):
            Mail(recipient = True, sender = True, body = None)

    def test_mail_has_a_default_subject(self):
        self.assertEqual(Mail(recipient = True, sender = True, body = True).subject, 'Missing subject')
