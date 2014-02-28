from functools import wraps
import json
import string

from flask import Response

import linux_info


def to_underscore(dash_input):
    """
    translates a string with dash to underscore instead.

    eg. some-thing to some_thing
    """
    table = string.maketrans('-', '_')
    return str(dash_input).translate(table)


def get_info_function(info_name):
    if hasattr(linux_info, info_name):
        fn = getattr(linux_info, info_name)
    return fn


def as_json(fn):
    @wraps(fn)
    def wrapper(**args):
        resp = fn(**args)
        return Response(json.dumps(resp), status=200,
                        mimetype='application/json')
    return wrapper
