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


def num_cores():
    return psutil.NUM_CPUS


def load_avg():
    with open('/proc/loadavg') as proc_file:
        content = proc_file.read()

    # the first 3 columns are the loadavg for the last 1, 5, 15 minutes
    averages = content.split()[0:3]
    result = []
    for average in averages:
        average = float(average)
        percentage_load = (average * 100) / num_cores()
        result.append([average, int(percentage_load)])
    return result
