import subprocess
from controller import Controller

class CrawlerController(Controller):
    
    def __init__(self):
        super(CrawlerController, self).__init__()

    def crawl(self):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        subprocess.call("./scripts/run-all-spiders.sh", shell=True)
        return self.redirect(self.url_for('board.control_panel'))
