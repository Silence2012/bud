#!/usr/bin/env python
import os
import sys
from setuptools import setup
ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)


exec(open('agent/version.py').read())

setup(
name = 'moon',
author = 'SimonSun',
author_email = '386488135@qq.com',
description = 'a monitor agent',
version = version,
packages = ['agent'],
install_requires=['websocket-client==0.11.0',
'requests==2.2.1',
'tornado==2.2.1'],
scripts = ['bin/moon'],
data_files = [
('/etc/init.d',['moon']),
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
