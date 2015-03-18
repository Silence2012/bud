import tornado.ioloop
import tornado.web
import json
from handle import Handle
from container import Container
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
class getCpu(tornado.web.RequestHandler):
    def get(self):
        self.handle =Handle()
        self.write(json.dumps(self.handle.getCpu()))
class getMem(tornado.web.RequestHandler):
    def get(self):
        self.handle = Handle()
        self.write(json.dumps(self.handle.getMem()))
class getBlk(tornado.web.RequestHandler):
    def get(self):
        self.handle = Handle()
        self.write(json.dumps(self.handle.getBlk()))
class getNet(tornado.web.RequestHandler):
    def get(self):
        self.handle = Handle()
        self.write(json.dumps(self.handle.getNet()))
app= tornado.web.Application([
(r"/v1/",MainHandler),
(r"/v1/runContainerId",ContainerHandler),
(r"/v1/getArg",getContainerArg),
(r"/v1/container/cpu",getCpu),
(r"/v1/container/mem",getMem),
(r"/v1/container/blkio",getBlk),
(r"/v1/container/net",getNet),
])
if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
