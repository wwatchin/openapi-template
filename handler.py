# ------------------------------------------------------------------------------
# handler.py - Acts as an intermediary between main.py and other routines.
# Copyright (C) 2023 kWatanabe (@wwatchin)
# This file is licensed by MIT License. See "LICENSE".
# ------------------------------------------------------------------------------

from models import *
from error import *

def do_validation(token):
    if token != "TOKEN":
        raise AuthorizationError("Invalid token.", 401)
    return {}

def do_get_token(body):
    return TokenPostResponse(token="TOKEN")

def do_post_resouce(userinfo, action, id, body):
    return ResourceIdPostResponse(date="DATE", result="RESULT")
