#!/usr/bin/env python
import os
import sys
from setuptools import setup
ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
if sys.version_info[0] == 3:
    requirements_file = './requirements3.txt'
else:
    requirements_file = './requirements.txt'

exec(open('agent/version.py').read())

with open(requirements_file) as requirements_txt:
    requirements = [line for line in requirements_txt]

setup(
name = 'monitor-agent',
author = 'SimonSun',
author_email = '386488135@qq.com',
description = 'a monitor agent',
version = version,
packages = ['agent'],
install_requires=requirements,
scripts = ['./moon'],
data_file = [
('/etc/init.d',['bin/moon']),
],
classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)
