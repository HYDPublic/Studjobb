# -*- coding: utf-8 -*-
import unittest 
from src.job.job   import Job 
from src.job.title import TitleException 

class TestJobTitle(unittest.TestCase):

    def test_title_in_constructor(self):
        job = Job(title = "Javascript-programmer")
        self.assertEqual(job.title, "Javascript-programmer")

    def test_title_has_a_default_string(self):
        job = Job()
        self.assertEqual(job.title, "Mangler tittel")

    def test_title_capitalized(self):
        job = Job("javascript-programmer")
        self.assertEqual(job.title, "Javascript-programmer")

    def test_title_trimmed(self):
        job = Job("  Javascript-programmer   ")
        self.assertEqual(job.title, "Javascript-programmer")

    def test_title_should_not_lowercase_other_characters(self):
        job = Job("Javascript-programmer at DNB")
        self.assertEqual(job.title, "Javascript-programmer at DNB")
        
    def test_title_removes_linebreaks(self):
        job = Job("Javascript-programmer\nWith angular experience!")
        self.assertEqual(job.title, "Javascript-programmer With angular experience!")

    def test_title_raises_error_when_title_is_too_short(self):
        tooShortTitle = 'short'
        self.assertRaises(TitleException, Job, tooShortTitle)

    def test_title_raises_error_when_title_is_too_long(self):
        tooLongTitle = "Javascript-programmer" * 10
        self.assertRaises(TitleException, Job, tooLongTitle)

    def test_title_raises_error_when_title_contains_html(self):
        titleWithHTML = "<b>Javascript-programmer</b>"
        self.assertRaises(TitleException, Job, titleWithHTML)

    def test_title_raises_error_when_title_contains_nested_html(self):
        titleWithHTML = "<script<script>>Javascript-programmer"
        self.assertRaises(TitleException, Job, titleWithHTML)

    def test_title_raises_error_when_title_is_not_a_string(self):
        titleThatsNotAString = object() 
        self.assertRaises(TitleException, Job, titleThatsNotAString)

    def test_title_raises_error_when_title_contains_non_printable_characters(self):
        titleWithWeirdCharacters = "ǝlʇᴉʇ pɹᴉǝʍ ɐ sᴉ sᴉɥʇ"
        self.assertRaises(TitleException, Job, titleWithWeirdCharacters)

    def test_title_with_scandinavian_characters(self):
        titleWithScandinavianCharacters = "Javascript-programmer på ÆØÅ"
        job = Job(titleWithScandinavianCharacters)
        self.assertEqual(job.title, titleWithScandinavianCharacters)

