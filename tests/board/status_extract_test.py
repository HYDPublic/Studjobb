# -*- coding: utf-8 -*-
import unittest 
import datetime
from src.board.board import Board
from src.job.job     import Job 

class TestBoardStatusExtract(unittest.TestCase):

    def test_board_can_extract_jobs_by_status(self):
        jobs = [Job(status = 'pending'), Job(status = 'active'), Job(status = 'active')]
        board = Board(jobs = jobs)
        self.assertEqual(len(board.jobs_by_status('pending')), 1)

    def test_board_ignores_expired_jobs_when_extracting_by_status(self):
        jobs = [Job(due_date=datetime.date(1991, 4, 20), status = 'dead')]
        board = Board(jobs = jobs)
        self.assertEqual(len(board.jobs_by_status('dead')), 1)

    def test_board_returns_no_jobs_if_no_jobs_are_in_board(self):
        board = Board()
        self.assertEqual(len(board.jobs_by_status('dead')), 0)
