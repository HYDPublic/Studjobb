from controller import Controller

class ErrorController(Controller):
    
    def __init__(self, database):
        pass

    def not_found(self, error):
        return self.render('404.html'), 404
