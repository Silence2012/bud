#!/usr/bin/env python
import json
from Metric import Metric
class Handle(object):
    def getMetric(self):        
        con = Metric()
        ret = con.runContainerId()
        dt = {}
        for i in ret:
            dt4 = {}
#            dt1,dt2,dt3,dt4 = {},{},{},{}
            con.setFilePath(i)
#            dt1['cpuAcct'] = con.cpuAcct()
#            dt2['memStat'] = con.memStat()
#            dt3['blkio'] = con.blkio()
            dt4['netStat'] = con.netStat()
#            dt[i] = [dt1,dt2,dt3,dt4]
            dt[i] = [dt4]
        return dt
if __name__ == '__main__':
   print "="*80+"start"+"="*80
   obj = Handle()
   print obj.getMetric()
   print "="*80+"end"+"="*80
