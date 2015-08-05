# -*- coding: utf-8 -*-
import unittest 
from src.job.job         import Job 
from src.job.description import DescriptionException 

class TestJobDescription(unittest.TestCase):

    def test_description_in_constructor(self):
        job = Job(description = "We are looking for a guru")
        self.assertEqual(job.description, "We are looking for a guru")

    def test_description_by_default_is_string(self):
        job = Job()
        self.assertEqual(job.description, "Mangler beskrivelse")

    def test_description_can_not_contain_intrusive_html_tags(self):
        self.assertRaises(DescriptionException, Job, None, "<script>document.alert('Vennligst søk snarest!');</script>")



