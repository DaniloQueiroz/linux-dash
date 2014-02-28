from datetime import datetime
from subprocess import run

import psutil


def hostname():
    return run('/bin/hostname').stdout.strip()


def current_time():
    return datetime.now().strftime("%a, %d. %b %Y %H:%M")


def uptime():
    uptime = datetime.now() - datetime.fromtimestamp(psutil.get_boot_time())
    return str(uptime)


def os_info():
    distro = run('/usr/bin/lsb_release -ds').stdout
    kernel = run('/bin/uname -r').stdout
    return '%s %s' % (distro, kernel)
