# -*- coding: utf-8 -*-
import re

class TemplateError(Exception):
    pass

class Template(object):

    def __init__(self, text, variables = {}):
        self.text = text
    
    def format(self, variables_with_values):
        variables_remaining_in_template = self.variables
         
        for variable in variables_with_values:
            value = variables_with_values[variable]
            self.text = self.text.replace('%' + variable + '%', value)

            if variable in variables_remaining_in_template:
                variables_remaining_in_template.remove(variable)

        if variables_remaining_in_template:
            raise TemplateError('Undefined variables in template.')

    @property
    def variables(self):
        variable_matches = re.findall('\%([a-zA-Z]*)\%', self.text)
        variable_matches = filter(None, variable_matches)
        variable_matches = list(set(variable_matches))
        return variable_matches
