# -*- coding: utf-8 -*-
import re

class TemplateError(Exception):
    pass

class Template(object):

    def __init__(self, text, variables = {}, title = 'Untitled', job = None):
        self.text  = text
        self.title = title
        self.job   = job

        self.user_defined_variables     = variables
        self.template_defined_variables = self.extract_variables(text) 
        
        if self.job:
            self.job_properties = self.extract_properties_from_job(job)
            self.merge_user_defined_variables_with_job_properties()

        self.format()

    @staticmethod
    def extract_properties_from_job(job):
        job_properties = {
            "job.title":    job.title,
            "job.place":    job.place,
            "job.position": job.position,
            "job.company":  job.company
        }
        # Removes job properties that evaluates to False
        return dict((k, v) for k, v in job_properties.iteritems() if v)
        
    def merge_user_defined_variables_with_job_properties(self):
        part_one = self.job_properties.items()
        part_two = self.user_defined_variables.items()
        self.user_defined_variables = dict(part_one + part_two)

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
