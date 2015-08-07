# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.board.board import Board
from src.job.job     import Job 

class TestBoardFilter(unittest.TestCase):

    def test_board_can_filter_out_expired_jobs(self):
        jobs = [Job(due_date=datetime.date(1993, 4, 20))]
        board = Board(jobs = jobs, filterExpiredJobs = True)
        self.assertEqual(len(board.jobs), 0)
