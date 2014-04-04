from flask import Blueprint, abort
from flask.templating import render_template

from lnx_dash.util import as_json, to_underscore, get_info_function


dash = Blueprint('dash', __name__)


@dash.route('/')
def dashboard():
    return render_template('index.html')


@dash.route('/api/<info_name>')
@as_json
def api_call(info_name):
    info_name = to_underscore(info_name)

    fn = get_info_function(info_name)
    if fn:
        return fn()
    else:
        abort(404)
