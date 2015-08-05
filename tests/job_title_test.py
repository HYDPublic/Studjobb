import unittest 
from src.job import Job 
from src.job import TitleException 

class TestJob(unittest.TestCase):

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
