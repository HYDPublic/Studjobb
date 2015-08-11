# -*- coding: utf-8 -*-
import unittest 
from src.job.job import Job 

class TestJobPosition(unittest.TestCase):

    def test_position_is_ukjent_by_default(self):
        self.assertEqual(Job().position, "Ukjent")
