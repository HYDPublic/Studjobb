import socket

class Prisoner(object):

    def __init__(self, ip, user_id):
        if self.is_valid_ip(ip):
            self.ip = ip
        self.user_id = user_id
        self.sentence = None

    @property
    def __hash__(self):
        return (self.ip, self.user_id)
    
    @staticmethod
    def is_valid_ip(ip):
        return socket.inet_aton(ip)
