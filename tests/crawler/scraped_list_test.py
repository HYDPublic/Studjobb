# -*- coding: utf-8 -*-
import unittest 
from src.crawler.scraped_job  import ScrapedJob 
from src.crawler.scraped_list import ScrapedList

class TestScrapedList(unittest.TestCase):
    
    def test_list_has_zero_scraped_jobs_by_default(self):
        self.assertEqual(len(ScrapedList().scraped_jobs), 0)
    
    def test_list_can_set_scraped_jobs_in_constructor(self):
        scraped_jobs = [ScrapedJob(), ScrapedJob(), ScrapedJob()]
        scraped_list = ScrapedList(scraped_jobs = scraped_jobs)
        self.assertEqual(len(scraped_list.scraped_jobs), 3)
