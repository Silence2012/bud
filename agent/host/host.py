#!/usr/bin/env python
import psutil as p
from collections import OrderedDict
class Hostinfo(object):
    ''' Return the information in /proc/cpuinfo 
        as a dictionary 
    '''
    def __init__(self):
        self.cpuinfo = OrderedDict()
        self.procinfo = OrderedDict()
        self.cpuno = 0
#   get the other system info
    def getOsinfo(self):
        return {'users':p.users(),'boot_time':p.boot_time()}

#   get the cpu percent used with psutil
    def getpCpuPercent(self):
        self.ret = p.cpu.percent(interval=1,percpu=True)
        return {'cpupercent':self.ret}

#   get the mem used with psutil          
    def getpMem(self):
        self.ret_virt = p.virtual_memory()
        self.ret_swap = p.swap_memory()
        return {'virtual_mem':self.ret_virt,'swap_mem':self.ret_swap}

#   get the disk information used with psutil
    def getpDisk(self):
        self.disk_part = p.disk_partitions()
        self.disk_usage = p.disk_usage('/')
        self.disk_io_counters = p.disk_io_counters(perdisk=False)
        return {'disk_part':self.disk_part,'disk_usage':self.disk_usage,'disk_io_counters':self.disk_io_counters}

#   get the network information used with psutil
    def getpNet(self):
        self.net_io_counters = p.net_io_counters(pernic=True)
        self.net_connections = p.net_connections()
        return {'net_io_counters':self.net_io_counters,"net_connections":self.net_connections}

#   get the cpu memssage from the interface of '/proc/cpuinfo'
    def getCpu(self):
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
    def getMem(self):
        meminfo = OrderedDict()
        try:
            with open('/proc/meminfo') as f:
                for line in f:
                    meminfo[line.split(":")[0]] = line.split(":")[1].strip()
        except Exception,e:
            print "Unexcept error :", e
        finally:
            return meminfo
    def getNet(self):
        netinfo = OrderedDict()                   
        try:
            with open('/proc/net/dev') as f:
                for line in f:
                    if line.strip().startswith('Inter'):
                        pass
                    elif line.strip().startswith('face'):
                        pass
                    else :
                        temp = OrderedDict()
                        temp['receive_bytes'] = line.strip().split(':')[1].split()[0]
                        temp['transmit_bytes'] = line.strip().split(':')[1].split()[8]
                        netinfo[line.strip().split(':')[0]] = temp
        except Exception,e:
            print "unexcept error",e
        finally:
            return netinfo
    def getDisk(self):
        diskinfo = OrderedDict()
        try:
            with open('/proc/diskstats') as f:
                for line in f:
                    temp = OrderedDict()
                    temp['read_total'] = line.split()[6].strip()
                    temp['write_total'] = line.split()[10].strip()
                    temp['io_process'] = line.split()[11].strip()
                    temp['io_time'] = line.split()[12].strip()
                    diskinfo[line.split()[2].strip()] = temp
        except Exception,e:
            print "Unexcept error" , e
        finally:
            return diskinfo
  
if __name__ == "__main__":
    ins = Hostinfo()
    print ins.getpMem()
   # print ins.getDisk()
   # print ins.getCpu()
   # print "*"*80
   # print ins.getMem()

                    

