from controller import Controller

class ErrorController(Controller):
    
    def __init__(self, database):
        super(ErrorController, self).__init__()

    def not_found(self, error):
        return self.render('404.html'), 404

    def exception(self, exception):
        return self.render('500.html', message = exception.message), 500
