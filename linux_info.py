from datetime import datetime
from functools import wraps
import json
from subprocess import run

from flask.blueprints import Blueprint
from flask.wrappers import Response
import psutil


linux_info_api = Blueprint('linux_info_api', __name__)


def as_json(fn):
    @wraps(fn)
    def wrapper(*args):
        resp = fn(*args)
        return Response(json.dumps(resp), status=200,
                        mimetype='application/json')
    return wrapper


@linux_info_api.route('/hostname')
@as_json
def hostname():
    return run('/bin/hostname').stdout.strip()


@linux_info_api.route('/current_time')
@as_json
def now():
    return datetime.now().strftime("%a, %d. %b %Y %H:%M")


@linux_info_api.route('/uptime')
@as_json
def uptime():
    uptime = datetime.now() - datetime.fromtimestamp(psutil.get_boot_time())
    return str(uptime)


@linux_info_api.route('/os_info')
@as_json
def osinfo():
    distro = run('/usr/bin/lsb_release -ds').stdout
    kernel = run('/bin/uname -r').stdout
    return '%s %s' % (distro, kernel)
