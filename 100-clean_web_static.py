#!/usr/bin/python3
"""deletes out-of-date archives
"""
import os
from fabric.api import run, local, env


env.hosts = ["35.229.34.27", "35.237.166.174"]


def do_clean(number=0):
    """
    deletes out-of-date archives
    - If number is 0 or 1, keep only the most recent version of your
        archiveives.
    - if number is 2, keep the most recent, and second most recent versions
        of your archive.
    - etc.
    """
    n = 1 if number == 0 else number
    files_to_delete = sorted(os.listdir("versions/"))[:-n]
    for file in files_to_delete:
        local("rm ./{}".format(file))
    delete = run("ls -ltr /data/web_static/releases").split()[:-n]
    for f in delete:
        run("rm -rf ./{}".format(f))
