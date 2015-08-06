# -*- coding: utf-8 -*-
import unittest 
from src.job.job         import Job 
from src.job.description import DescriptionException 

class TestJobDescription(unittest.TestCase):

    def test_description_in_constructor(self):
        job = Job(description = "We are looking for a guru")
        self.assertEqual(job.description, "We are looking for a guru")

    def test_description_by_default_is_string(self):
        self.assertEqual(Job().description, "Mangler beskrivelse")

    def test_description_can_not_contain_intrusive_html_tags(self):
        self.assertRaisesRegexp(DescriptionException, 'html', Job, description = "<script>document.alert('Vennligst søk snarest!');</script>")

    def test_description_only_disallows_html_tags_not_tagnames(self):
        Job(description = "script iframe img")

    def test_description_raises_exception_if_valid_and_invalid_html_tags_in_same_description(self):
        self.assertRaisesRegexp(DescriptionException, 'html', Job, description = "<b>Hey!</b><iframe src=''></iframe>")

    def test_description_can_contain_non_intrusive_html_tags(self):
        job = Job(description = "<strong>Søk nå!</strong>")
        self.assertEqual(job.description, "<strong>Søk nå!</strong>")

    def test_description_can_not_be_longer_than_1000_words(self):
        self.assertRaisesRegexp(DescriptionException, 'long', Job, description = "This is really five words\n" * 200)
