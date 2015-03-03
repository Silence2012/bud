import tornado.ioloop
import tornado.web
import json
from handle import Handle
from docker import Client
from container import Container
class getContainerArg(tornado.web.RequestHandler):
    def get(self):
        con = Container()
        ret = con.getContainerArg()
        self.write(json.dumps(ret))
class ContainerHandler(tornado.web.RequestHandler):
    def get(self):
        con = Container()
        ret_con = con.getContainer()
        self.write(json.dumps(ret_con))
        #self.write(json.dumps(con.containers()))
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        handle =Handle()
        self.write(json.dumps(handle.getMetric()))
application = tornado.web.Application([
(r"/",MainHandler),
(r"/getContainer",ContainerHandler),
(r"/getArg",getContainerArg),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
