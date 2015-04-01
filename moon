#!/usr/bin/python
import threading
import tornado.ioloop
from agent import app
app.listen(8888)
t = threading.Thread(tornado.ioloop.IOLoop.instance().start())
t.daemon = True
t.start()
