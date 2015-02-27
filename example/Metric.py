#!/usr/bin/env python
import re
import os
import commands
from collections import OrderedDict
from docker import Client
class Metric(object):
    def __init__(self):
        self.con = Client()

    def runContainerId(self):
        con_id_list = []
        for items in self.con.containers():
            con_id_list.append(items[u'Id'])       
        return con_id_list
    def setFilePath(self,container_id):
        self.container_id = container_id
        self.cpuacct_path = '/cgroup/cpuacct/lxc/%s/cpuacct.stat' % self.container_id
        self.memStat_path = '/cgroup/memory/lxc/%s/memory.stat' % self.container_id
        self.blkio_path = '/cgroup/blkio/lxc/%s/' % self.container_id
        self.netStat_path = '/cgroup/devices/lxc/%s/' % self.container_id
    def cpuAcct(self):
        cpuDict = OrderedDict()
        with open(self.cpuacct_path) as f:
            dt = {}
            for line in f:
                templist = line.split()
                cpuDict[templist[0]] = templist[1]
            dt['cpuAcct'] = cpuDict
        return dt
    def memStat(self):
        memDict = OrderedDict()
        with open(self.memStat_path)as f:
            dt = {}
            for line in f:
                m = re.search(r"(rss|swap)\s+(\d+)",line)
                if m:
                    memDict[m.group(1)] = int(m.group(2))
            dt['memStat'] = memDict
        return dt
    def blkio(self):
        blkioDict =  OrderedDict()
        with open(self.blkio_path+'blkio.io_wait_time') as f:
            dt = {}
            for line in f:
                templist = line.split()
                blkioDict['io_wait_time'] = {templist[0]:templist[1]}
            dt['blkioStat'] = blkioDict
        return dt
    def netStat(self):
        netDict = OrderedDict()
        with open(self.netStat_path+'tasks') as f:
            tpid = f.readline()
            tpid = tpid[:-1]       
            filename = '/var/run/netns'+self.container_id
            if not os.path.exists(filename):
                if not os.path.exists('/var/run/netns'):
                    os.mkdir(r'/var/run/netns')
                    (status,output) = commands.getstatusoutput('ln -s /proc/'+tpid+'/ns/net'+' '+'/var/run/netns/'+self.container_id) 
        try :
            (status_ns,output_ns) = commands.getstatusoutput('ip netns exec '+self.container_id+' ifconfig eth0 | grep "RX bytes"')
        except e:
            print e
        ret = OrderedDict()
        m = re.findall(r"(:\d+)",output_ns)
        m1 = []
        for i in m:
            i = i.strip(':')
            m1.append(i)
        dt1 = {}
        if m1:
            dt1["RX bytes"] = m1[0]
            dt1["TX bytes"] = m1[1]  
        ret["netStat"] = dt1
        return ret
        
