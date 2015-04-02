#!/usr/bin/python
import threading
import tornado.ioloop
from agent import app
import logging
logging.basicConfig(filename='/var/log/moon.log',level=logging.DEBUG)
app.listen(8888)
t = threading.Thread(tornado.ioloop.IOLoop.instance().start())
t.daemon = True
logging.debug(t.start())
