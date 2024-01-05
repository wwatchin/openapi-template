# ------------------------------------------------------------------------------
# error.py - Error and exception classes and handling routines.
# Copyright (C) 2024 kWatanabe (@wwatchin)
# This file is licensed by MIT License. See "LICENSE".
# ------------------------------------------------------------------------------

class WebappException(Exception):
    def __init__ (self, message="A internal error occurred.", status_code=500):
        super(WebappException, self).__init__(message)
        self.message = message
        self.code = status_code

class AuthorizationError (WebappException):
    pass
