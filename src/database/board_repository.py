from src.board.board import Board
from job_repository  import JobRepository 

class BoardRepository(object):

    def __init__(self, database):
        self._database = database

    def find(self):
        job_repository = JobRepository(self._database)
        jobs = job_repository.findAll()
        return Board(jobs = jobs, sortByAttribute = 'due_date')

    def save(self):
        pass

    def remove(self):
        pass
