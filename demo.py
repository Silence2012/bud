#!/usr/bin/env python
import os
tmp = os.popen('docker ps -q').readlines()
print tmp
for item in tmp:
	print item.strip()
