import unittest 
from src.job import Job 

class TestJob(unittest.TestCase):

    def test_title_capitalized(self):
        job = Job("javascript-programmer")
        assert job.title == "Javascript-programmer"

    def test_title_trimmed(self):
        job = Job("  Javascript-programmer   ")
        assert job.title == "Javascript-programmer"

