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

    def test_title_must_be_longer_than_5_characters(self):
        self.assertRaises(TitleException, Job, 'title')

