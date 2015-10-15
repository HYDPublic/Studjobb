# -*- coding: utf-8 -*-
import unittest 
import mock
from mock import MagicMock
from src.crawler.robot import Robot 
from src.crawler.robot import AlreadyVisitedError 

class TestRobot(unittest.TestCase):

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

    @mock.patch('src.crawler.robot.Robot.user_agent')
    @mock.patch('src.crawler.robot.requests')
    def test_robot_uses_GET_requests_by_default(self, requests_library, user_agent):
        robot = Robot()
        robot.request('http://website.com/page/101')
        assert requests_library.request.call_args[1]['method'] == 'GET'

    @mock.patch('src.crawler.robot.Robot.user_agent')
    @mock.patch('src.crawler.robot.requests')
    def test_robot_can_use_POST_requests(self, requests_library, user_agent):
        robot = Robot()
        robot.request('http://website.com/page/101', method = 'POST')
        assert requests_library.request.call_args[1]['method'] == 'POST'

    @mock.patch('src.crawler.robot.Robot.user_agent')
    @mock.patch('src.crawler.robot.requests')
    def test_robot_remembers_visited_urls(self, requests_library, user_agent):
        robot = Robot()
        robot.request('http://website.com/page/101')
        assert robot.visited_urls[0] == 'http://website.com/page/101'
