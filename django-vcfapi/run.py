#!/usr/bin/env python3


# import os
# import pexpect
# import sys
# import time
# import datetime
# import paramiko
import subprocess


proc = subprocess.Popen("python3 setup.py sdist", shell=True)
return_code = proc.wait()

proc = subprocess.Popen(
    "pip3 install --force-reinstall -U dist/django-vcfapi-0.1.tar.gz",
    shell=True)
return_code = proc.wait()
