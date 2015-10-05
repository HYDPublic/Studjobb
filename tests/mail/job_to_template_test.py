# -*- coding: utf-8 -*-
import unittest 
from src.job.job       import Job
from src.mail.template import Template 
from src.mail.template import TemplateError

class TestJobToTemplate(unittest.TestCase):

    def test_job_properties_can_be_referenced_when_job_is_provided_to_template(self):
        template = Template('Your job is titled: %job.title%')
        template.job = Job(title = 'Developer', place = 'Oslo', position = 'Deltid')
        self.assertEqual(template.text, 'Your job is titled: Developer')

    def test_job_properties_are_not_replaced_when_property_is_none(self):
        template = Template('Your job is at: %job.place%')
        template.job = Job(title = 'Developer', place = None, position = 'Deltid')
        self.assertEqual(template.text, 'Your job is at: %job.place%')

    def test_multiple_job_properties_can_be_referenced_in_template(self):
        template = Template('Your job is titled: %job.title% and is %job.position% type job.')
        template.job = Job(title = 'Developer', place = 'Trondheim', position = 'Fulltid')
        self.assertEqual(template.text, 'Your job is titled: Developer and is Fulltid type job.')

    def test_job_can_be_loaded_after_object_has_been_constructed(self):
        template = Template('Your job is titled: %job.title% and is %job.position% type job.')
        template.job = Job(title = 'Developer', place = 'Trondheim', position = 'Fulltid')
        self.assertEqual(template.text, 'Your job is titled: Developer and is Fulltid type job.')
