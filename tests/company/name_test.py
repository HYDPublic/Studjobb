# -*- coding: utf-8 -*-
import unittest 
from src.company.company import Company
from src.company.name    import NameException 


class TestCompanyName(unittest.TestCase):

    def test_name_in_constructor(self):
        company = Company(name = "BEKK")
        self.assertEqual(company.name, "BEKK")

    def test_name_can_not_contain_bold_html_tags(self):
        company = Company(name = "BEKK")
        self.assertRaisesRegexp(NameException, "HTML", Company, name = "<b>BEKK</b>")

    def test_name_can_not_contain_em_html_tags(self):
        company = Company(name = "BEKK")
        self.assertRaisesRegexp(NameException, "HTML", Company, name = "<em>BEKK</em>")

    def test_name_can_not_contain_header_html_tags(self):
        company = Company(name = "BEKK")
        self.assertRaisesRegexp(NameException, "HTML", Company, name = "<h1>BEKK</h1>")

    def test_name_trims_whitespace(self):
        company = Company(name = "    Visma    ")
        self.assertEqual(company.name, "Visma")

    def test_name_has_default(self):
        self.assertEqual(Company(name = None).name, "Mangler navn")

    def test_name_does_capitalize_first_letter_like_a_title(self):
        self.assertEqual(Company(name = "mckinsey").name, "mckinsey")
