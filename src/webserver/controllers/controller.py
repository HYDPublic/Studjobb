from flask import make_response, render_template, abort, request, redirect, url_for, g
from src.webserver.authentication import Authentication
from src.database.engine import database

class Controller(object):
    
    def __init__(self):
        self.authentication = Authentication(database)
        self.request        = request
        self.render         = render_template
        self.abort          = abort
        self.request        = request
        self.redirect       = redirect 
        self.url_for        = url_for 

    def user_is_authenticated(self):
        request_header = request.headers.get('Authorization')
        if not self.authentication.is_valid_authentication_format(request_header):
            return False
        
        encoded_credentials = self.authentication.extract_encoded_credentials(request_header)
        decoded_credentials = self.authentication.decode_credentials(encoded_credentials)
        credentials = self.authentication.split_credentials(decoded_credentials) 
    
        return self.authentication.verify_credentials(credentials['username'], credentials['password'])

    def prompt_for_password(self):
        response = make_response(self.render('admin/unauthenticated.html'), 401)
        response_header = self.authentication.authenticate_response_header()
        response.headers['WWW-Authenticate'] = response_header
        return response
