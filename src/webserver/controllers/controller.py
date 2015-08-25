from flask import render_template, abort, request, redirect, url_for, g

class Controller(object):
    
    def __init__(self):
        self.request  = request
        self.render   = render_template
        self.abort    = abort
        self.request  = request
        self.redirect = redirect 
        self.url_for  = url_for 
        self.g        = g
