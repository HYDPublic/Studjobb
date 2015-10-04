from sqlalchemy.sql import text
from src.mail.template import Template

class TemplateRepository(object):

    def __init__(self, database):
        self._database = database
        self._table = 'templates'

    def find(self, id):
        result = self._database.execute('select * from %s where id = %d' % (self._table, int(id)))
        row = result.fetchone()
        return Template(id = row.id, title = row.title, text = row.text)

    def findAll(self):
        result = self._database.execute('select * from %s' % (self._table))
        templates = []
        for row in result:
            templates.append(Template(id = row.id, title = row.title, text = row.text))
        return templates 

    def save(self, template):
        if template.id is None:
            return self.create(template)
        else:
            return self.update(template)

    def update(self, template):
        result = self._database.execute(text('update templates set title = :title, text = :text where id = :id'),
            title = template.title,
            text =  template.text,
            id    = template.id 
        )
        return self.find(template.id) 

    def create(self, template):
        result = self._database.execute(text('insert into templates set title = :title, text = :text'),
            title = template.title,
            text  = template.text
        )
        template.id = result.lastrowid
        return template

    def remove(self, template):
        pass
