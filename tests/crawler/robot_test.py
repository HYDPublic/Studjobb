# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.crawler.robot import Robot 
from src.crawler.robot import AlreadyVisitedError 

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.patcher = mock.patch('src.crawler.robot.config')
        self.mock_config = self.patcher.start()

    def tearDown(self):
        self.addCleanup(self.patcher.stop)

    def test_robot_has_no_visited_urls_by_default(self):
        assert len(Robot().visited_urls) == 0

    def test_visited_website_is_not_scraped(self):
        robot = Robot()
        robot.visited_urls = ['http://website.com/page/1']
        with self.assertRaises(AlreadyVisitedError):
            robot.visit('http://website.com/page/1') 

    def test_invalid_url_raises_exception(self):
        robot = Robot()
        with self.assertRaises(ValueError):
            robot.visit('tp:/invalid-url')

    def test_visit_calls_request(self):
        robot = Robot()
        robot.request = MagicMock()
        robot.visit('http://website.com/page/3')
        assert robot.request.called

    @mock.patch('src.crawler.robot.requests')
    def test_robot_uses_GET_requests_by_default(self, requests_library):
        robot = Robot()
        robot.request('http://website.com/page/101')
        assert requests_library.request.call_args[1]['method'] == 'GET'

    @mock.patch('src.crawler.robot.requests')
    def test_robot_can_use_POST_requests(self, requests_library):
        robot = Robot()
        robot.request('http://website.com/page/101', method = 'POST')
        assert requests_library.request.call_args[1]['method'] == 'POST'

    @mock.patch('src.crawler.robot.requests')
    def test_robot_remembers_visited_urls(self, requests_library):
        robot = Robot()
        robot.request('http://website.com/page/101')
        assert robot.visited_urls[0] == 'http://website.com/page/101'

    @mock.patch('src.crawler.robot.requests')
    def test_robot_uses_a_proxy_for_every_request(self, requests_library):
        self.mock_config.return_value = "http://proxy.com:8080"
        robot = Robot()
        robot.request('http://website.com/page/155')
        assert requests_library.request.call_args[1]['proxies']['http']  == 'http://proxy.com:8080'
        assert requests_library.request.call_args[1]['proxies']['https'] == 'http://proxy.com:8080'
