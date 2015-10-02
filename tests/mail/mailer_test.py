# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.mail.mail import Mail
from src.mail.mailer import Mailer 

class TestMailer(unittest.TestCase):

    @mock.patch('src.mail.mailer.Mailer.turn_mail_into_message')
    @mock.patch('src.mail.mailer.Mailer.reconnect')
    @mock.patch('src.mail.mailer.Mailer.is_connection_alive')
    def test_mailer_tries_to_reconnect_if_server_disconnected(self, mock_is_alive, mock_reconnect, mock_message):
        mailer = Mailer()
        mailer.server = MagicMock()
        mock_message.return_value = '' 
        mock_is_alive.return_value = False
        mailer.send(MagicMock())
        assert mock_reconnect.called

    @mock.patch('src.mail.mailer.Mailer.turn_mail_into_message')
    @mock.patch('src.mail.mailer.Mailer.reconnect')
    @mock.patch('src.mail.mailer.Mailer.is_connection_alive')
    def test_mailer_does_not_reconnect_if_connected(self, mock_is_alive, mock_reconnect, mock_message):
        mailer = Mailer()
        mailer.server = MagicMock()
        mock_message.return_value = '' 
        mock_is_alive.return_value = True 
        mailer.send(MagicMock())
        assert not mock_reconnect.called

    def test_message_contains_to_header_with_correct_value(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', body = 'Hello world')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('to: recipient@domain.com\n' in message, True)

    def test_message_contains_to_header_with_name_if_provided(self):
        mail = Mail(recipient = 'recipient@domain.com', recipient_name = 'Uncle Bob', sender = 'sender@domain.com', body = 'Hello world')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('to: Uncle Bob <recipient@domain.com>\n' in message, True)

    def test_message_contains_from_header_with_correct_value(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', body = 'Hello world')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('from: sender@domain.com\n' in message, True)

    def test_message_contains_from_header_with_name_if_provided(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', sender_name = 'Billy Bob', body = 'Hello world')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('from: Billy Bob <sender@domain.com>\n' in message, True)

    def test_message_contains_subject_header_with_correct_value(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', body = 'Hello world', subject = 'Hola!')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('subject: =?utf-8?q?Hola!?=\n' in message, True)

    def test_message_contains_body_with_correct_value(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', body = 'Hello world', subject = 'Hola!')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('\n\nSGVsbG8gd29ybGQ=' in message, True)

    def test_message_can_contain_subject_with_scandinavian_characters(self):
        mail = Mail(recipient = 'recipient@domain.com', sender = 'sender@domain.com', body = 'Hello world', subject = 'Hællæ bællå ålø!')
        message = Mailer.turn_mail_into_message(mail)
        self.assertEqual('subject: =?utf-8?b?SMOmbGzDpiBiw6ZsbMOlIMOlbMO4IQ==?=\n' in message, True)
