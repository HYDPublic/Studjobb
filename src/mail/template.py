# -*- coding: utf-8 -*-
import re

class TemplateError(Exception):
    pass

class Template(object):

    def __init__(self, text, variables = {}, title = 'Untitled'):
        self.text = text
        self.title = title

        self.user_defined_variables = variables
        self.template_defined_variables = self.extract_variables(text) 

        self.format()

    def format(self):
        variables_remaining_in_template = self.template_defined_variables
         
        for variable in self.user_defined_variables:
            value = self.user_defined_variables[variable]
            self.text = self.text.replace('%' + variable + '%', value)

            if variable in variables_remaining_in_template:
                variables_remaining_in_template.remove(variable)

        if variables_remaining_in_template:
            raise TemplateError('Undefined variables in template.')

    @staticmethod
    def extract_variables(text):
        variable_matches = re.findall('\%([a-zA-Z]*)\%', text)
        variable_matches = filter(None, variable_matches)
        variable_matches = list(set(variable_matches))
        return variable_matches
