#!/usr/bin/env python
import json
from metric import Metric
from container import Container
class Handle(object):
    def getMetric(self):    
        con = Container()
        ret = con.runContainerId()
        dt = {}
        for i in ret:
            dt1,dt2,dt3,dt4 = {},{},{},{}
            con.setFilePath(i)
            data = Metric(con.container_id,con.cpuacct_path,con.memStat_path,con.blkio_path,con.netStat_path)
            data.getNetns()
            dt1['cpuAcct'] = data.cpuAcct()
            dt2['memStat'] = data.memStat(i)
            dt3['blkio'] = data.blkio()
            dt4['netStat'] = data.netStat()
            dt[i] = [dt1,dt2,dt3,dt4]
        return dt
if __name__ == '__main__':
   print "="*80+"start"+"="*80
   obj = Handle()
   print obj.getMetric()
   print "="*80+"end"+"="*80
