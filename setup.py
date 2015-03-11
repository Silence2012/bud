from setuptools import setup
setup(
name = 'monitor-agent',
author = 'SimonSun',
author_email = '386488135@qq.com',
description = 'a monitor agent',
version = '0.1.1-dev',
packages = ['agent',],
scripts = ['./moon'],
data_file = [
('/etc/init.d',['bin/moon']),
],
install_requires=[
    "flask",
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
