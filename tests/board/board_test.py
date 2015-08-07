# -*- coding: utf-8 -*-
import unittest 
from src.board.board import Board
from src.job.job     import Job 

class TestBoard(unittest.TestCase):
    
    def test_board_has_zero_jobs_by_default(self):
        self.assertEqual(len(Board().jobs), 0)
    
    def test_board_can_set_jobs_in_constructor(self):
        jobs = [Job(), Job(), Job()]
        board = Board(jobs = jobs)
        self.assertEqual(len(board.jobs), 3)

    def test_board_can_sort_jobs_by_title(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs, sortBy = "title")
        self.assertEqual(board.jobs[0].title, "Aaaaaa")

    def test_board_ignores_sort_if_attribute_does_not_exist(self):
        jobs = [Job(title="cccccc"), Job(title="bbbbbb"), Job(title="aaaaaa")]
        board = Board(jobs = jobs, sortBy = "non_existent_attribute")
        self.assertEqual(board.jobs[0].title, "Cccccc")

