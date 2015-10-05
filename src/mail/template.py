# -*- coding: utf-8 -*-
import re

class TemplateError(Exception):
    pass

class Template(object):

    def __init__(self, text, title = 'Untitled', subject = 'Missing subject', id = None):
        self.id                          = id
        self._text                       = text
        self._job                        = None
        self.title                       = title
        self.subject                     = subject

        self._user_defined_variables     = {}
        self._template_defined_variables = self.extract_variables(text) 

    @property
    def job(self):
        return self._job
        
    @job.setter
    def job(self, job):
        variables_from_job  = self.extract_properties_from_job(job)
        variables_from_user = self._user_defined_variables
        self._user_defined_variables = self.merge(variables_from_job, variables_from_user)

    @property
    def text(self):
        return self.compile()

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def variables(self):
        return self._user_defined_variables

    @variables.setter
    def variables(self, variables):
        self._user_defined_variables = variables

    def compile(self):
        compiled = self._text 
        for variable, value in self._user_defined_variables.iteritems():
            compiled = compiled.replace('%' + variable + '%', value)
        return compiled

    @staticmethod
    def extract_properties_from_job(job):
        job_properties = {
            "job.title":    job.title,
            "job.place":    job.place,
            "job.position": job.position,
            "job.company":  str(job.company) if job.company else None
        }
        # Removes job properties that evaluates to False
        return dict((k, v) for k, v in job_properties.iteritems() if v)

    @staticmethod
    def merge(first_dict, second_dict):
        return dict(first_dict.items() + second_dict.items())

    @staticmethod
    def extract_variables(text):
        variable_matches = re.findall('\%([a-zA-Z]*)\%', text)
        variable_matches = filter(None, variable_matches)
        variable_matches = list(set(variable_matches))
        return variable_matches
