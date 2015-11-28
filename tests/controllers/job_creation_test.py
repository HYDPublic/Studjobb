from mock import MagicMock
import unittest
from src.webserver.controllers.job import JobController

def mock_job_controller(job_controller):
    job_controller.redirect = \
    job_controller.url_for = \
    job_controller.job_repository = \
    job_controller.prompt_for_password = \
    job_controller.get_job_from_request = MagicMock()
    return job_controller

class TestJobCreation(unittest.TestCase):

    def test_job_is_saved_when_user_is_authenticated(self):
        controller = mock_job_controller(JobController(database = None))
        controller.user_is_authenticated = MagicMock(return_value = True)
        controller.create()
        assert controller.job_repository.save.called == True

    def test_job_is_not_saved_when_user_is_not_authenticated(self):
        controller = mock_job_controller(JobController(database = None))
        controller.user_is_authenticated = MagicMock(return_value = False)
        controller.create()
        assert controller.job_repository.save.called == False
