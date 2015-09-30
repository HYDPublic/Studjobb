# -*- coding: utf-8 -*-
import os
import smtplib
from email import message
from smtplib import SMTPServerDisconnected 
from ConfigParser import SafeConfigParser

class Mailer(object):

    def __init__(self):
        self.server = None
        self.config = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'config'))

    def smtp_credentials(self):
        config = SafeConfigParser()
        config.read(self.config)
        return {
            'username': config.get('smtp', 'username'),
            'password': config.get('smtp', 'password')
        }

    def connect(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)

    def authenticate(self):
        self.server.ehlo()
        self.server.login(
            self.smtp_credentials()['username'],
            self.smtp_credentials()['password']
        )  

    def disconnect(self):
        self.server.close()

    def is_connection_alive(self):
        try:
            return self.server.docmd('NOOP')[0] == 250
        except SMTPServerDisconnected:
            return False

    def reconnect(self):
        self.disconnect()
        self.connect()

    @staticmethod
    def turn_mail_into_message(mail):
        message_to_be_sent =  message.Message()
        message_to_be_sent.add_header('to',      mail.recipient)
        message_to_be_sent.add_header('from',    mail.sender)
        message_to_be_sent.add_header('subject', mail.subject)
        message_to_be_sent.set_payload(mail.body)
        return message_to_be_sent.as_string()

    def send(self, mail = False):
        if self.is_connection_alive() == False:
            self.reconnect()
        
        message = self.turn_mail_into_message(mail)
        self.server.sendmail(mail.sender, mail.recipient, message)
