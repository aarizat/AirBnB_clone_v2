#!/usr/bin/python3
"""
Compress before sending.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compress a folder to .tgz archive.
    """
    date = datetime.utcnow()
    path = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)
    if local("mkdir -p versions").failed:
        return
    if local("tar -cvzf {} web_static".format(path)).failed:
        return
    return path
