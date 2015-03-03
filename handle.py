#!/usr/bin/env python
import json
from metric import Metric
class Handle(object):
    def getMetric(self):    
        con = Metric()
        ret = con.runContainerId()
        dt = {}
        for i in ret:
            dt1,dt2,dt3,dt4 = {},{},{},{}
            con.setFilePath(i)
            con.getNetns()
            dt1['cpuAcct'] = con.cpuAcct()
            dt2['memStat'] = con.memStat(i)
            dt3['blkio'] = con.blkio()
            dt4['netStat'] = con.netStat()
            dt[i] = [dt1,dt2,dt3,dt4]
        return dt
if __name__ == '__main__':
   print "="*80+"start"+"="*80
   obj = Handle()
   print "="*80+"end"+"="*80
