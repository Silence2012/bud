from docker import Client
class Container(object):
    def __init__(self):
        self.con = Client()
    def getContainer(self):
        ret = self.con.containers()
        return ret
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
