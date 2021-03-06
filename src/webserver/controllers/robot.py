from controller import Controller
from flask import Response
import os

class RobotController(Controller):
    
    def __init__(self, database):
        super(RobotController, self).__init__()

    def get_path_to_asset(self, filename):
        path_to_asset = os.path.join(__file__, '..', '..', 'assets', filename)
        return os.path.abspath(path_to_asset)

    def get_file_contents(self, path_to_file):
        content = ''
        with open(path_to_file, 'r') as asset_content:
            content += asset_content.read()
        return content

    def sitemap(self):
        path_to_sitemap_dot_xml = self.get_path_to_asset('sitemap.xml')
        response = self.get_file_contents(path_to_sitemap_dot_xml)
        return Response(response, status = 200, mimetype = "application/xml")

    def robots(self):
        path_to_robots_dot_txt = self.get_path_to_asset('robots.txt')
        response = self.get_file_contents(path_to_robots_dot_txt)
        return Response(response, status = 200, mimetype = "text/plain")
