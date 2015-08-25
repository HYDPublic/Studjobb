from flask import render_template, abort, request, redirect, url_for

class Controller(object):
    
    def __init__(self):
        self.render   = render_template
        self.abort    = abort
        self.request  = request
        self.redirect = redirect 
        self.request  = request
        self.url_for  = url_for 
