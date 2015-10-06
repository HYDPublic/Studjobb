# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.job.job import Job 
from src.job.job import JobException

class TestJobApplyLink(unittest.TestCase):

    def test_job_can_have_an_apply_url(self):
        job = Job(apply_url = 'http://company.com/apply')
        self.assertEqual(job.apply_url, 'http://company.com/apply')

    def test_job_apply_url_is_pound_sign_by_default(self):
        self.assertEqual(Job().apply_url, '#')
