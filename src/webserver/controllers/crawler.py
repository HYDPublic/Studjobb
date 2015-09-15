import subprocess
import os
from controller import Controller

class CrawlerController(Controller):
    
    def __init__(self):
        super(CrawlerController, self).__init__()

    def crawl(self):
        if not self.user_is_authenticated(): return self.prompt_for_password()
        current_dir  = os.path.dirname(os.path.realpath(__file__)) 
        scripts_dir  = os.path.join(current_dir, '..', '..', '..', 'scripts')
        crawl_script = os.path.join(scripts_dir, 'run-all-spiders.sh')
        subprocess.call(crawl_script, shell=True)
        return self.redirect(self.url_for('board.control_panel'))
