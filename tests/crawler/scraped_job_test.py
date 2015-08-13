# -*- coding: utf-8 -*-
import unittest 

from src.crawler.scraped_job import ScrapedJob

class TestScrapedJob(unittest.TestCase):

    def test_can_have_a_guid(self):
        self.assertEqual(ScrapedJob(guid = "4a7d3ce7620c3f9dd305303cf58f55e7").guid, "4a7d3ce7620c3f9dd305303cf58f55e7")

    def test_can_have_a_title_shorter_than_5_characters(self):
        self.assertEqual(ScrapedJob(title = "Short").title, "Short")

    def test_strips_html_tags_from_title(self):
        self.assertEqual(ScrapedJob(title = "<h1>Short</h1>").title, "Short")

    def test_description_can_contain_intrusive_html_tags(self):
        scraped_job = ScrapedJob(description = "<script>alert(1);</script>")
        self.assertEqual(scraped_job.description, "<script>alert(1);</script>")

    def test_description_can_be_longer_than_1000_words(self):
        ScrapedJob(description = "this is really five words\n" * 200)

    def test_company_is_only_a_string(self):
        self.assertEqual(ScrapedJob(company = "BEKK").company, "BEKK")

    def test_due_date_is_only_a_string(self):
        self.assertEqual(ScrapedJob(due_date = "Om 2 uker").due_date, "Om 2 uker")

