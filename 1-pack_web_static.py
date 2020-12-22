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
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(date, "%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(path)).failed:
        return
    return path
