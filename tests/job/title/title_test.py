# -*- coding: utf-8 -*-
import unittest 
from src.job.job   import Job 
from src.job.title import TitleException 
from src.job.title import Title 

class TestJobTitle(unittest.TestCase):

    def test_title_in_constructor(self):
        title = Title(text = "Javascript-programmer")
        self.assertEqual(str(title), "Javascript-programmer")

    def test_title_does_not_raise_a_index_error_with_empty_string(self):
        try: Title(text = '')
        except TitleException: pass

    def test_title_capitalized(self):
        title = Title(text = "javascript-programmer")
        self.assertEqual(str(title), "Javascript-programmer")

    def test_title_trimmed(self):
        title = Title(text = "  Javascript-programmer   ")
        self.assertEqual(str(title), "Javascript-programmer")

    def test_title_should_not_lowercase_other_characters(self):
        title = Title(text = "Javascript-programmer at DNB")
        self.assertEqual(str(title), "Javascript-programmer at DNB")
        
    def test_title_removes_linebreaks(self):
        title = Title(text = "Javascript-programmer\nWith angular experience!")
        self.assertEqual(str(title), "Javascript-programmer With angular experience!")

    def test_title_raises_error_when_title_is_too_short(self):
        tooShortTitle = 'short'
        self.assertRaises(TitleException, Title, text = tooShortTitle)

    def test_title_raises_error_when_title_is_too_long(self):
        tooLongTitle = "Javascript-programmer" * 10
        self.assertRaises(TitleException, Title, text = tooLongTitle)

    def test_title_raises_error_when_title_contains_html(self):
        titleWithHTML = "<b>Javascript-programmer</b>"
        self.assertRaises(TitleException, Title, text = titleWithHTML)

    def test_title_raises_error_when_title_contains_nested_html(self):
        titleWithHTML = "<script<script>>Javascript-programmer"
        self.assertRaises(TitleException, Title, text = titleWithHTML)

    def test_title_raises_error_when_title_is_not_a_string(self):
        titleThatsNotAString = 123 
        self.assertRaises(TitleException, Title, text = titleThatsNotAString)

    def test_title_with_scandinavian_characters(self):
        titleWithScandinavianCharacters = u"Javascript-programmer på ÆØÅ"
        title = Title(text = titleWithScandinavianCharacters)
        self.assertEqual(unicode(title), titleWithScandinavianCharacters)
