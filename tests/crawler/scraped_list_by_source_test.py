# -*- coding: utf-8 -*-
import unittest 
from src.crawler.scraped_job  import ScrapedJob 
from src.crawler.scraped_list import ScrapedList

class TestScrapedListBySource(unittest.TestCase):
    
    def test_scraped_list_can_extract_scraped_jobs_by_source(self):
        scraped_jobs = [ScrapedJob(source = 'one'), ScrapedJob(source = 'two'), ScrapedJob(source = 'three')]
        scraped_list = ScrapedList(scraped_jobs = scraped_jobs)
        self.assertEqual(len(scraped_list.scraped_jobs_from('one')), 1)

    def test_scraped_list_returns_empty_list_(self):
        scraped_jobs = [ScrapedJob(source = 'one'), ScrapedJob(source = 'two'), ScrapedJob(source = 'three')]
        scraped_list = ScrapedList(scraped_jobs = scraped_jobs)
        self.assertEqual(len(scraped_list.scraped_jobs_from('four')), 0)

    def test_scraped_list_can_return_a_list_of_all_the_sources(self):
        scraped_jobs = [ScrapedJob(source = 'one'), ScrapedJob(source = 'two'), ScrapedJob(source = 'three')]
        scraped_list = ScrapedList(scraped_jobs = scraped_jobs)
        self.assertEqual('one' in scraped_list.sources, True)
        self.assertEqual('two' in scraped_list.sources, True)
        self.assertEqual('three' in scraped_list.sources, True)

    def test_scraped_list_sources_does_not_contain_dupes(self):
        scraped_jobs = [ScrapedJob(source = 'one'), ScrapedJob(source = 'one'), ScrapedJob(source = 'three')]
        scraped_list = ScrapedList(scraped_jobs = scraped_jobs)
        self.assertEqual(len(scraped_list.sources), 2)
