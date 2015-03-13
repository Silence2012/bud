import tornado.ioloop
import tornado.web
import json
from handle import Handle
from container import Container
class getContainerArg(tornado.web.RequestHandler):
    def get(self):
        con = Container()
        dt = {}
        for item in con.runContainerId():
            ret = con.getContainerArg(item)
            dt[item]=ret
        self.write(json.dumps(dt))
class ContainerHandler(tornado.web.RequestHandler):
    def get(self):
        con = Container()
        ret_con = con.runContainerId()
        self.write(json.dumps(ret_con))
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        handle =Handle()
        self.write(json.dumps(handle.getMetric()))
app= tornado.web.Application([
(r"/",MainHandler),
(r"/runContainerId",ContainerHandler),
(r"/getArg",getContainerArg),
])
if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
