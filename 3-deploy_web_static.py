#!/usr/bin/python3
"""
Do complete deploy of the web static
"""
from fabric.api import env


env.hosts = ["35.229.34.27", "35.237.166.174"]

do_pack = __import__("1-pack_web_static").pack_web_static
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
