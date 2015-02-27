import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = [ " boy","girl","child"]
        self.render("template.html",title = "My title",items = items)
application = tornado.web.Application([
(r"/",MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
