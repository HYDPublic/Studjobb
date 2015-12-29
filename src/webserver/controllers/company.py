from controller import Controller
from flask import Response
import json

from src.company.company import Company 
from src.company.logo.logo import Logo
from src.company.logo.logofinder import LogoFinder, Google
from src.database.company_repository import CompanyRepository

class CompanyController(Controller):
    
    def __init__(self, database):
        self.company_repository = CompanyRepository(database) 
        super(CompanyController, self).__init__()

    @Controller.authentication_required
    def new(self):
        query = self.request.args.get('query', '')
        results = self.google_image_search(query)
        return self.render('admin/company/new.html', query=query, search_results=results) 

    @Controller.authentication_required
    def list(self):
        companies = self.company_repository.findAll()
        json_dict = {}
        for company in companies:
            json_dict[company.id] = company.name
        response = json.dumps(json_dict)
        return Response(response, status = 200, mimetype = "application/json")

    def google_image_search(self, query):
        if query:
            return LogoFinder(query).search(Google())
        else:
            return []

    @Controller.authentication_required
    def edit(self, id):
        company = self.company_repository.find(id)
        if not company: return self.abort(404)
        query = self.request.args.get('query', '')
        results = self.google_image_search(query)
        return self.render('admin/company/edit.html', query=query,company=company, search_results=results) 

    @Controller.authentication_required
    def create(self):
        company_name = self.request.form['name']
        logo_path    = self.request.form['logo'].encode('utf8')

        logo    = Logo(path = logo_path)
        company = Company(name = company_name, logo = logo) 
        company.logo.set_color_to_dominant_color_if_not_already_set()

        company = self.company_repository.save(company) 
        return self.redirect(self.url_for('company.edit', id = company.id))

    @Controller.authentication_required
    def update(self, id):
        company_name = self.request.form['name']
        logo_path    = self.request.form['logo'].encode('utf8')
        logo_color   = self.request.form['color']

        company      = self.company_repository.find(id)
        company.name = company_name
        company.logo = Logo(path = logo_path, color = logo_color)
        
        company = self.company_repository.save(company) 
        return self.redirect(self.url_for('company.edit', id = company.id))
