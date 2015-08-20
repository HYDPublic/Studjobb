# -*- coding: utf-8 -*-
import unittest 
from src.email.template import Template 
from src.email.template import TemplateError

class TestEmailTemplate(unittest.TestCase):

    def test_template_takes_text_in_constructor(self):
        template = Template('This is a template.')
        self.assertEqual(template.text, 'This is a template.')

    def test_template_can_replace_variables_with_values(self):
        template = Template('%firstname% %lastname%')
        template.format({'firstname': 'Michael', 'lastname': 'McMillan'})
        self.assertEqual(template.text, 'Michael McMillan')

    def test_template_can_replace_variables_with_values(self):
        template = Template('Hello %firstname% %lastname%!')
        template.format({'firstname': 'Michael', 'lastname': 'McMillan'})
        self.assertEqual(template.text, 'Hello Michael McMillan!')

    def test_template_can_contain_percentage_sign_without_a_defined_variables(self):
        template = Template('Hello %greeting% 5% remains!')
        template.format({'greeting': 'there'})
        self.assertEqual(template.text, 'Hello there 5% remains!')

    def test_template_variable_can_be_used_multiple_times(self):
        template = Template('Hello %name%. Do you like the name %name%?')
        template.format({'name': 'Michael'})
        self.assertEqual(template.text, 'Hello Michael. Do you like the name Michael?')

    def test_template_can_extract_variables_from_text(self):
        variables = Template('Hello %firstname%. You are %age% years old?').variables
        self.assertEqual('firstname' in variables, True)
        self.assertEqual('age'       in variables, True)

    def test_template_variable_extraction_ignores_doubled_percentages(self):
        variables = Template('Hello %%firstname%%. You are %age% years old?').variables
        self.assertEqual('age' in variables, True)

    def test_template_raises_exception_if_missing_variable(self):
        with self.assertRaisesRegexp(TemplateError, 'Undefined'):
            template = Template('Hello %name%. Do you like the name %name%?')
            template.format({'firstname': 'Michael'})

    @unittest.skip('')
    def test_template_can_have_variables(self):
        template = Template('This is a template with a %var%.', {
            'var': 'variable'    
        })
        self.assertEqual(template.text, 'This is a template variable.')
