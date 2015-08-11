from src.company.company import Company

class CompanyRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'companies'

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, id))
        row = result.fetchone()
        company = Company(name = row.name, logo = row.logo.encode('utf8'))
        return company 

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        companies = []
        for row in result:
            companies.append(Company(name = row.name, logo = row.logo))
        return companies 

    def save(self, company):
        pass

    def remove(self, company):
        pass
