#!/usr/bin/env python
from collections import OrderedDict
class Cpuinfo(object):
    ''' Return the information in /proc/cpuinfo 
        as a dictionary 
    '''
    def __init__(self):
        self.cpuinfo = OrderedDict()
        self.procinfo = OrderedDict()
        self.cpuno = 0
    def getData(self):
        try :
            with open('/proc/cpuinfo') as f:
                for line in f:
                    if not line.strip():
                        self.cpuinfo['proc%s' % self.cpuno] = self.procinfo
                        self.cpuno +=1
                        self.procinfo = {}
                    else:
                        if len(line.split(':')) == 2:
                            self.procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                        else :
                            self.procinfo[line.split(":")[0].strip()] = ''
        except Exception,e:
            print "Unexcept error :"
            print e
        finally:
            return self.cpuinfo
if __name__ == "__main__":
    ins = Cpuinfo()
    print ins.getData()

                    

