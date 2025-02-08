#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the web_static folder
"""
from fabric import task
import os
from datetime import datetime

@task
def do_pack(c):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    os.makedirs("versions", exist_ok=True)
    c.run(f"tar -czvf {archive_name} web_static")
