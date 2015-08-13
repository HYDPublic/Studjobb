# -*- coding: utf-8 -*-
import unittest 
from src.job.job import JobException
from src.job.job import Job 

class TestJobStatus(unittest.TestCase):

    def test_status_is_pending_by_default(self):
        job = Job()
        self.assertEqual(job.status, 'pending')

    def test_status_in_constructor(self):
        job = Job(status = 'active')
        self.assertEqual(job.status, 'active')

    def test_status_raises_error_if_not_a_recognized_error(self):
        with self.assertRaisesRegexp(JobException, 'status'):
            job = Job(status = 'bogus')

    def test_status_does_not_raise_error_if_valid_status_but_in_uppercase(self):
        job = Job(status = 'ACTIVE')
        self.assertEqual(job.status, 'active')

    def test_can_be_changed_outside_constructor(self):
        job = Job(status = 'active')
        job.status = 'pending'
        self.assertEqual(job.status, 'pending')

    def test_job_has_a_list_of_all_possible_statuses(self):
        self.assertEqual('active'  in Job().statuses, True)
        self.assertEqual('pending' in Job().statuses, True)
        self.assertEqual('dead'    in Job().statuses, True)
