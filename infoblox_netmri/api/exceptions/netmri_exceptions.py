class NotImplementedException(Exception):
    """Exception class for describing errors in API methods which haven't been implemented properly

       :param controller: API controller where a called method belongs to
       :param method: not implemented API method name"""

    def __init__(self, controller, method):
        self.controller = controller
        self.method = method

    def what(self):
        print("The method {} from the controller {} is not implemented!".format(self.method,
                                                                                self.controller))
