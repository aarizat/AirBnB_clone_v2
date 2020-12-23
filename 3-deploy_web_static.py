#!/usr/bin/python3
"""
Do complete deploy of the web static
"""
from datetime import datetime
from os import path
from fabric.api import put, run, env, local


env.hosts = ["35.229.34.27", "35.237.166.174"]


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


def do_deploy(archive_path):
    """
    distributes an archive to web servers

    Args:
        archive_path (str): has the form "versions/web_static_YMDHMS.tgz"
    """
    if not path.exists(archive_path):
        return False
    file_tar = archive_path.split("/")[-1]  # web_static_YMDHMS.tgz
    server_path = "/data/web_static/releases/{}".format(file_tar[:-4])
    run("mkdir -p {}".format(server_path))  # create path in the server
    put(archive_path, "/tmp/")  # copy from local to remote
    run("tar -xzf /tmp/{} -C {}".format(file_tar, server_path))
    run("rm /tmp/{}".format(file_tar))
    run("mv -f {}/web_static/* {}/".format(server_path, server_path))
    run('rm -rf {}/web_static'.format(server_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(server_path))
    return True


def deploy():
    """creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
