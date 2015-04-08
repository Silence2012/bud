#!/usr/bin/env python
from docker import Client
import os
c = Client()
lt = []
for item in c.containers():
    lt.append(item[u'Id'])
for i in lt:
    filename = '/var/run/netns/'+i
    try :
    #    with open(filename) as f:
    #        pass
        os.file(filename)
    except Exception,e:
        print 'with an error %s',e
        raise e
    else :
        print "no error" 

