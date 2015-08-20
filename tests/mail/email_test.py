# -*- coding: utf-8 -*-
import unittest 
from src.email.email import Email 
from src.email.email import EmailError

class TestEmail(unittest.TestCase):

    def test_email_needs_recipient(self):
        with self.assertRaisesRegexp(EmailError, 'recipient'):
            Email(recipient = None, sender = True, body = True)

    def test_email_needs_sender(self):
        with self.assertRaisesRegexp(EmailError, 'sender'):
            Email(recipient = True, sender = None, body = True)

    def test_email_needs_a_body(self):
        with self.assertRaisesRegexp(EmailError, 'body'):
            Email(recipient = True, sender = True, body = None)

    def test_email_has_a_default_subject(self):
        self.assertEqual(Email(recipient = True, sender = True, body = True).subject, 'Missing subject')
