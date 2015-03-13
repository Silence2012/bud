from docker import Client
class Container(object):
    def __init__(self):
        self.con = Client()
    def runContainerId(self):
        run_conId_list = []
        for items in self.con.containers():
            run_conId_list.append(items[u'Id'])
        return run_conId_list
    def setFilePath(self,container_id):
        self.container_id = container_id
        self.cpuacct_path = '/cgroup/cpuacct/lxc/%s/cpuacct.stat' % self.container_id
        self.memStat_path = '/cgroup/memory/lxc/%s/memory.stat' % self.container_id
        self.blkio_path = '/cgroup/blkio/lxc/%s/' % self.container_id
        self.netStat_path = '/cgroup/devices/lxc/%s/' % self.container_id
    def getContainerArg(self,cid):
        ret = self.con.inspect_container(cid)        
        ret = ret[u'Config']
        return  ret
if __name__ == "__main__":
    con = Container()
    print con.getContainer()
    print "+"*80
    for i in con.getContainer():
        print con.getContainerArg(i)
        print "-"*80
