from sqlalchemy.sql      import text
from src.company.company import Company

class CompanyRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'companies'

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, id))
        row = result.fetchone()
        company = Company(id = row.id, name = row.name, logo = row.logo.encode('utf8'))
        return company 

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        companies = []
        for row in result:
            companies.append(Company(id = row.id, name = row.name, logo = row.logo))
        return companies 

    def save(self, company):
        result = self._database.execute(text('update companies set name = :title where id = :id'),
            title = company.name,
            id    = company.id 
        )
        return self.find(company.id) 

    def remove(self, company):
        pass
