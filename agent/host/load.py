#!/usr/bin/env python
from collections import OrderedDict
def getData():
    loadavg = OrderedDict()
    with open('/proc/loadavg') as f:
        for line in f:
            con = line.split()
            loadavg['lavg_1'] = con[0]
            loadavg['lavg_5'] = con[1]
            loadavg['lavg_15'] = con[2]
            loadavg['now/total'] = con[3]
            loadavg['lastpid'] = con[4]
    return loadavg
print getData()
