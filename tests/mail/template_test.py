# -*- coding: utf-8 -*-
import unittest 
from src.mail.template import Template 
from src.mail.template import TemplateError

class TestEmailTemplate(unittest.TestCase):

    def test_template_has_a_default_title(self):
        template = Template('This is a template with a default title.')
        self.assertEqual(template.title, 'Untitled')

    def test_template_has_a_default_subject(self):
        template = Template('This is a template with a default title.')
        self.assertEqual(template.subject, 'Missing subject')

    def test_template_has_a_default_subject(self):
        template = Template('This is a template with a default title.', subject = 'Subject')
        self.assertEqual(template.subject, 'Subject')

    def test_template_can_override_default_title(self):
        template = Template('This is a template with a defined title.', title = 'Title')
        self.assertEqual(template.title, 'Title')

    def test_template_takes_text_in_constructor(self):
        template = Template('This is a template.')
        self.assertEqual(template.text, 'This is a template.')

    def test_template_can_replace_variables_with_values(self):
        template = Template('%firstname% %lastname%')
        template.variables = {'firstname': 'Michael', 'lastname': 'McMillan'} 
        self.assertEqual(template.text, 'Michael McMillan')

    def test_template_can_replace_variables_with_values(self):
        template = Template('Hello %firstname% %lastname%!')
        template.variables = {'firstname': 'Michael', 'lastname': 'McMillan'}
        self.assertEqual(template.text, 'Hello Michael McMillan!')

    def test_template_can_contain_percentage_sign_without_a_defined_variables(self):
        template = Template('Hello %greeting% 5% remains!')
        template.variables = {'greeting': 'there'}
        self.assertEqual(template.text, 'Hello there 5% remains!')

    def test_template_variable_can_be_used_multiple_times(self):
        template = Template('Hello %name%. Do you like the name %name%?')
        template.variables = {'name': 'Michael'}
        self.assertEqual(template.text, 'Hello Michael. Do you like the name Michael?')

    def test_template_can_extract_variables_from_text(self):
        variables = Template.extract_variables('Hello %firstname%. You are %age% years old?')
        self.assertEqual('firstname' in variables, True)
        self.assertEqual('age'       in variables, True)

    def test_template_variable_extraction_ignores_doubled_percentages(self):
        variables = Template.extract_variables('Hello %%firstname%%. You are %age% years old?')
        self.assertEqual('age' in variables, True)

    def test_template_variables_still_work_over_multiple_lines(self):
        template = Template("Hello %firstname%!\n Is your lastname %lastname%?")
        template.variables = {'firstname': 'Michael', 'lastname': 'McMillan'}
        self.assertEqual(template.text, 'Hello Michael!\n Is your lastname McMillan?')
