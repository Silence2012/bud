import tornado.ioloop
import tornado.web
import json
from handle import Handle
from container import Container
handle = Handle()
class getContainerArg(tornado.web.RequestHandler):
   # handle = Handle()
    def get(self):
        con = Container()
        dt = {}
        for item in con.runContainerId():
            ret = con.getContainerArg(item)
            dt[item]=ret
        self.write(json.dumps(dt))
class ContainerHandler(tornado.web.RequestHandler):
   # handle = Handle()
    def get(self):
        con = Container()
        ret_con = con.runContainerId()
        self.write(json.dumps(ret_con))
class MainHandler(tornado.web.RequestHandler):
    #handle =Handle()
    def get(self):
        self.write(json.dumps(handle.getMetric()))
class getCpu(tornado.web.RequestHandler):
   # handle =Handle()
    def get(self):
        self.write(json.dumps(handle.getCpu()))
class getMem(tornado.web.RequestHandler):
   # handle = Handle()
    def get(self):
        self.write(json.dumps(handle.getMem()))
class getBlk(tornado.web.RequestHandler):
   # handle = Handle()
    def get(self):
        self.write(json.dumps(handle.getBlk()))
class getNet(tornado.web.RequestHandler):
   # handle = Handle()
    def get(self):
        self.write(json.dumps(handle.getNet()))
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
