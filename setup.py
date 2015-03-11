from distutils.core import setup
setup(
name = 'monitor-agent',
author = 'SimonSun',
author_email = '386488135@qq.com',
description = 'a monitor agent',
version = '0.1.1-dev',
packages = ['agent','web'],
install_requires=[
    "flask",
],
)
