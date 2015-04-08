#!/bin/sh

# #############################################
# Copyright (c) 2014-2034 letv Inc. All rights reserved.
# #############################################
#
# Name:  build.sh
# Date:  2014-07-17 08:32
# Author:  sunxiaoning 
# Email:   sunxiaoning@letv.com
# Desc:  
#
#

python setup.py bdist_rpm --bdist-base tmp --binary-only --requires python-requests,python-websockify,docker-py,python-tornado,python-flask
