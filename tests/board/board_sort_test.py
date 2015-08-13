# -*- coding: utf-8 -*-
import unittest 
from src.board.board import Board
from src.job.job     import Job 

class TestBoardSorting(unittest.TestCase):

    def test_board_does_not_sort_by_default(self):
        jobs = [Job(title="xxxxxx"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs)
        self.assertEqual(board.jobs[0].title, "Xxxxxx")

    def test_board_can_sort_jobs_by_title(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs)
        sorted_jobs = board.jobs_sorted_by(attribute = 'title')
        self.assertEqual(sorted_jobs[0].title, "Aaaaaa")

    def test_board_ignores_sort_if_attribute_does_not_exist(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs)
        not_sorted_jobs = board.jobs_sorted_by(attribute = 'non-existent-field')
        self.assertEqual(not_sorted_jobs[0].title, "Cccccc")
