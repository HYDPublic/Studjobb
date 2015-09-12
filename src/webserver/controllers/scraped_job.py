from controller import Controller

from src.crawler.scraped_job import ScrapedJob 
from src.database.scraped_job_repository import ScrapedJobRepository
from src.database.company_repository import CompanyRepository

class ScrapedJobController(Controller):
    
    def __init__(self, database):
        self.scraped_job_repository = ScrapedJobRepository(database) 
        self.company_repository = CompanyRepository(database) 
        super(ScrapedJobController, self).__init__()

    def edit(self, guid):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        scraped_job = self.scraped_job_repository.find(guid)
        companies = self.company_repository.findAll()

        if not scraped_job: return self.abort(404)
        return self.render('admin/scraped_job/edit.html', scraped_job = scraped_job, companies = companies) 

    def update(self, guid):
        if not self.user_is_authenticated(): return self.prompt_for_password()

        # This will always be a delete action
        self.scraped_job_repository.remove(guid)
        return self.redirect(self.url_for('board.control_panel'))
