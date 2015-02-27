import tornado.ioloop
import tornado.web
import json
from Handle import Handle
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        handle =Handle()
        self.write(json.dumps(handle.getMetric()))
application = tornado.web.Application([
(r"/",MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
