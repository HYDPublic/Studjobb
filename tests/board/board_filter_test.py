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

    def test_board_can_ignore_filtering_out_expired_jobs(self):
        jobs = [Job(due_date=datetime.date(1991, 4, 20))]
        board = Board(jobs = jobs, filterExpiredJobs = False)
        self.assertEqual(len(board.jobs), 1)

    def test_board_filters_out_expired_jobs_by_default(self):
        jobs = [Job(due_date=datetime.date(1992, 4, 20))]
        board = Board(jobs = jobs)
        self.assertEqual(len(board.jobs), 0)
