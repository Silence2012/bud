import tornado.ioloop
import tornado.web
import json
from container.handle import Handle
from container.container import Container
from host.cpu import Cpuinfo
class getContainerArg(tornado.web.RequestHandler):
    def get(self):
        self.handle = Handle()
        self.con = Container()
        self.dt = {}
        for item in self.con.runContainerId():
            self.ret = self.con.getContainerArg(item)
            self.dt[item]= self.ret
        self.write(json.dumps(self.dt))
class ContainerHandler(tornado.web.RequestHandler):
    def get(self):
        self.handle = Handle()
        self.con = Container()
        self.ret_con = self.con.runContainerId()
        self.write(json.dumps(self.ret_con))
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.handle =Handle()
        self.write(json.dumps(self.handle.getMetric()))
class getMetric(tornado.web.RequestHandler):
    def get(self,name):
        self.handle = Handle()
        lt = ["cpu","mem","blkio","net"]
        if name in lt:
            if name == "cpu":
                ret = self.handle.getCpu()
            elif name == "mem":
                ret = self.handle.getMem()
            elif name == "blkio":
                ret = self.handle.getBlk()
            else :
                ret = self.handle.getNet()
        self.write(json.dumps(ret))
class getbyIdMetric(tornado.web.RequestHandler):
    def get(self,id,name):
        self.handle = Handle()
        self.con = Container()
        for item in self.con.getContainerTrucId():
            if id == item:
                if name == "cpu":
                     ret = self.handle.getCpu()[id]
                if name == "mem":
                     ret = self.handle.getMem()[id]
                if name == "blkio":
                     ret = self.handle.getBlk()[id]
                if name == "net":
                     ret = self.handle.getNet()[id]
        self.write(json.dumps(ret))
class getHost(tornado.web.RequestHandler):
    def get (self,name):
        self.ins = Cpuinfo()
        if name == "cpu":
            ret = self.ins.getData()
        else :
            ret = "Waiting for a moment "
        self.write(json.dumps(ret))
                
app= tornado.web.Application([
(r"/v1/",MainHandler),
(r"/v1/runContainerId",ContainerHandler),
(r"/v1/getArg",getContainerArg),
(r"/v1/container/([a-zA-Z]+)",getMetric),
(r"/v1/container/([0-9a-zA-Z]+)/([a-zA-Z]+)",getbyIdMetric),
(r"/v1/host/([a-z]+)",getHost),
])
if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
