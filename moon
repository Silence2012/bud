#!/usr/bin/python
import tornado.ioloop
from agent import app
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
