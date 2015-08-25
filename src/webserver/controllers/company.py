from controller import Controller

from src.company.company import Company 
from src.database.company_repository import CompanyRepository

class CompanyController(Controller):
    
    def __init__(self, database):
        self.company_repository = CompanyRepository(database) 
        super(CompanyController, self).__init__()

    def new(self):
        return self.render('admin/company/new.html') 

    def edit(self, id):
        company = self.company_repository.find(id)
        if not company: return self.abort(404)
        return self.render('admin/company/edit.html', company = company) 

    def create(self):
        company = Company() 
        company.name = self.request.form['name']
        company.logo = self.request.form['logo'].encode('utf8')
        company = self.company_repository.save(company) 
        return self.redirect(self.url_for('company.edit', id = company.id))

    def update(self, id):
        company = self.company_repository.find(id)
        company.name = self.request.form['name']
        company.logo = self.request.form['logo'].encode('utf8')
        company = self.company_repository.save(company) 
        return self.redirect(self.url_for('company.edit', id = company.id))
