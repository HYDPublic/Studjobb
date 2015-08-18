# -*- coding: utf-8 -*-
import unittest 
from src.job.job import Job 

class TestJobPlace(unittest.TestCase):

    def test_place_is_ukjent_by_default(self):
        self.assertEqual(Job().place, "Ukjent")
