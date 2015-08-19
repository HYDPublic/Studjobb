# -*- coding: utf-8 -*-
import unittest 
from src.job.job import Job 
from src.job.job import JobException

class TestJobHasAHiddenURLForEditing(unittest.TestCase):

    def test_job_gets_assinged_a_unique_url_for_editing(self):
        edit_urls = []
        for i in range(0, 100):
            edit_url = Job().edit_url
            self.assertEqual(edit_url in edit_urls, False)
            edit_urls.append(edit_url)

    def test_job_can_override_its_unique_url(self):
        job = Job()
        job.edit_url = 'some-random-url'
        self.assertEqual(job.edit_url, 'some-random-url')
