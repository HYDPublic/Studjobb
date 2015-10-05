from sqlalchemy.sql      import text
from src.company.company import Company

class CompanyRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'companies'

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, int(id)))
        row = result.fetchone()
        company = Company(id = row.id, name = row.name, logo = row.logo.encode('utf8'), color = row.color)
        return company 

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        companies = []
        for row in result:
            companies.append(Company(id = row.id, name = row.name, logo = row.logo.encode('utf8'), color = row.color))
        return companies 

    def save(self, company):
        if company.id is None:
            return self.create(company)
        else:
            return self.update(company)

    def update(self, company):
        result = self._database.execute(text('update companies set name = :name, logo = :logo, color = :color where id = :id'),
            name  = company.name,
            logo  = company.logo.filename,
            color = company.logo.color,
            id    = company.id 
        )
        return self.find(company.id) 

    def create(self, company):
        result = self._database.execute(text('insert into companies set name = :name, logo = :logo, color = :color'),
            name  = company.name,
            color = company.logo.color,
            logo  = company.logo.filename
        )
        company.id = result.lastrowid
        return company

    def remove(self, company):
        pass
