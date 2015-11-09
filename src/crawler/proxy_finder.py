import os
import subprocess
DEVNULL = open(os.devnull, 'wb')

class ProxyFinder(object):

    def __init__(self):
        self.script = "./elite_proxy_finder.py"
        self.args   = ["-q", "-s", "1"]

    def find_proxy(self):
        process = subprocess.Popen([self.script] + self.args, stdout=subprocess.PIPE, stderr=DEVNULL)
        (output, err) = process.communicate()
        process_flag = process.wait()
        return output.rstrip()

#print ProxyFinder().find_proxy()
