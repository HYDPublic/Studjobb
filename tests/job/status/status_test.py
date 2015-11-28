# -*- coding: utf-8 -*-
import unittest 
from src.job.status import StatusException
from src.job.status import Status

class TestStatus(unittest.TestCase):

    def test_code_in_constructor(self):
        status = Status(code = 'active')
        self.assertEqual(str(status), 'active')

    def test_is_pending_if_no_code_provided(self):
        status = Status(code = None)
        self.assertEqual(str(status), 'pending')

    def test_status_raises_error_if_not_a_recognized_error(self):
        with self.assertRaisesRegexp(StatusException, 'status'):
            Status(code = 'bogus')

    def test_status_does_not_raise_error_if_valid_status_but_in_uppercase(self):
        Status(code = 'ACTIVE')
