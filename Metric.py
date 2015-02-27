#!/usr/bin/env python
import re
import os
import commands
import subprocess
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
    #Get the container net namespace
    def getNetns(self):
        with open(self.netStat_path+'tasks') as f:
            tpid = f.readline()
            tpid = tpid[:-1]       
            filename = '/var/run/netns/'+self.container_id
            if not os.path.exists('/var/run/netns/'):
                os.mkdir(r'/var/run/netns')
            if  os.path.exists(filename):
                (status_file,output_file) = commands.getstatusoutput('rm -rf'+' '+filename) 
            (status,output) = commands.getstatusoutput('ln -s /proc/'+tpid+'/ns/net'+' '+filename)
    #Get the network value of container with the command ifconfig 
    def netStat(self):
        netDict = {}
        p = subprocess.Popen('ip netns exec'+' '+self.container_id+' '+'ifconfig',stdout=subprocess.PIPE,shell=True)
        ret_if = p.communicate()[0]
        netData = (i for i in ret_if.split('\n\n') if i and not i.startswith('lo'))
        netAda = re.compile(r'(eth[\d]*|p[\w]*|br[\d]*|veth[\w]*)')
        ipaddr = re.compile(r'(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}')
        macaddr = re.compile(r'[A-F0-9a-f:]{17}')
        RX_byte = re.compile(r'(RX bytes[\d:]*)')
        TX_byte = re.compile(r'(TX bytes[\d:]*)')
        for i in netData:
            x = {}
            if netAda.match(i):
                device = netAda.match(i).group()
            if ipaddr.search(i):
                ip = ipaddr.search(i).group() 
                x['ip'] = ip
            else:
                x['ip'] = None
            if macaddr.search(i):
                mac = macaddr.search(i).group()
                x['mac'] = mac
            if RX_byte.search(i):
                RX = RX_byte.search(i).group()[9:]
                x['RX_byte'] = RX
            if TX_byte.search(i):
                TX = TX_byte.search(i).group()[9:]
                x['TX_byte'] = TX
            netDict[device] = x
        return netDict 
        
if __name__ == '__main__':
    con = Metric()
    id_list = con.runContainerId()
    dt = {}
    for item in id_list:
        con.setFilePath(item)        
        con.getNetns()
        dt4 = con.netStat()
        print dt4
        dt[item] = [dt4]
    print dt
