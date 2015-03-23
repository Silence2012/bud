#!/usr/bin/env python
import json
from metric import Metric
from container import Container
class Handle(object):
    def __init__(self):
        self.con = Container()
        self.ret = self.con.runContainerId()
        self.dt,self.dt1,self.dt2,self.dt3,self.dt4 = {},{},{},{},{}
        for i in self.ret:
            self.con.setFilePath(i)
            self.data = Metric(self.con.container_id,self.con.cpuacct_path,self.con.memStat_path,self.con.blkio_path,self.con.netStat_path)
            self.data.getNetns()
            self.dt_cpu,self.dt_mem,self.dt_blk,self.dt_net = {},{},{},{}
            self.dt_cpu['cpuAcct'] = self.data.cpuAcct()
            self.dt_mem['memStat'] = self.data.memStat(i)
            self.dt_blk['blkio'] = self.data.blkio()
            self.dt_net['netStat'] = self.data.netStat()
            # we set the trunc id for the metric
            _i = i[:12]
            self.dt[_i]= [self.dt_cpu,self.dt_mem,self.dt_blk,self.dt_net]
            self.dt1[_i] = [self.dt_cpu]
            self.dt2[_i] = [self.dt_mem]
            self.dt3[_i] = [self.dt_blk]
            self.dt4[_i] = [self.dt_net]
    def getMetric(self):    
        return self.dt
    def getCpu(self):
        return self.dt1
    def getMem(self):
        return self.dt2   
    def getBlk(self):
        return self.dt3
    def getNet(self):
        return self.dt4
if __name__ == '__main__':
   print "="*80+"start"+"="*80
   obj = Handle()
   print obj.getMetric()
   print "*"*100
   print obj.getCpu()
   print "*"*100
   print obj.getMem()
   print "*"*100
   print obj.getBlk()
   print "*"*100
   print obj.getNet()
   print "="*80+"end"+"="*80
