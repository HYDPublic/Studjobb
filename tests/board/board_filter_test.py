# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.board.board import Board
from src.job.job     import Job 

class TestBoardFilter(unittest.TestCase):

    def test_board_can_filter_out_expired_jobs(self):
        jobs = [Job(title="Aaaaaa", due_date=datetime.date(1993, 4, 20))]
        board = Board(jobs = jobs)
        self.assertEqual(board.jobs[0].title, "Aaaaaa")
