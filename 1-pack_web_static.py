#!/usr/bin/python3
"""generates .tgz archive """
from fabric.api import local
from datetime import datetime


def do_pack():
    "generates .tgz archive"
    local("mkdir -p versions")
    timeNow = datetime.now()
    tgz = "versions/web_static_"
    tgz += "{}{}{}".format(timeNow.year, timeNow.month, timeNow.day)
    tgz += "{}{}{}".format(timeNow.hour, timeNow.minute, timeNow.second)
    tgz += ".tgz"
    result = "tar -cvzf "
    result += tgz
    result += " web_static"
    if local(result) == 1:
        return None
    return tgz
