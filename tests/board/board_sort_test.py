# -*- coding: utf-8 -*-
import unittest 
from src.board.board import Board
from src.job.job     import Job 

class TestBoardSorting(unittest.TestCase):

    def test_board_can_sort_jobs_by_title(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs, sortByAttribute = "title")
        self.assertEqual(board.jobs[0].title, "Aaaaaa")

    def test_board_ignores_sort_if_attribute_does_not_exist(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs, sortByAttribute = "non_existent_attribute")
        self.assertEqual(board.jobs[0].title, "Cccccc")
