# -*- coding: utf-8 -*-
import unittest 
from src.job.description import Description 
from src.job.description import DescriptionException 

class TestDescription(unittest.TestCase):

    def test_description_in_constructor(self):
        description = Description(text = "We are looking for a guru")
        self.assertEqual(str(description), "We are looking for a guru")

    def test_description_can_not_contain_intrusive_html_tags(self):
        self.assertRaisesRegexp(DescriptionException, 'html', Description, text = "<script>document.alert('Vennligst søk snarest!');</script>")

    def test_description_only_disallows_html_tags_not_tagnames(self):
        Description(text = "script iframe img")

    def test_description_raises_exception_if_valid_and_invalid_html_tags_in_same_description(self):
        self.assertRaisesRegexp(DescriptionException, 'html', Description, text = "<b>Hey!</b><iframe src=''></iframe>")

    def test_description_raises_exception_containing_a_list_of_the_invalid_html_tags(self):
        self.assertRaisesRegexp(DescriptionException, 'script.*iframe|iframe.*script', Description, text = "<script></script><iframe></iframe>")

    def test_description_can_contain_non_intrusive_html_tags(self):
        description = Description(text = "<strong>Søk nå!</strong>")
        self.assertEqual(str(description), "<strong>Søk nå!</strong>")

    def test_description_can_not_be_longer_than_1500_words(self):
        self.assertRaisesRegexp(DescriptionException, 'long', Description, text = "This is really five words\n" * 350)
