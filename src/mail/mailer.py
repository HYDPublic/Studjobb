import smtplib 

class Mailer(object):

    def __init__(self):
        self.server = smtplib.SMTP()
        
    def send(self, mail):
        pass

    def connect_to_server(self):
        server.connect(server, port)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(send_from, send_to, msg)
        server.close()

        
