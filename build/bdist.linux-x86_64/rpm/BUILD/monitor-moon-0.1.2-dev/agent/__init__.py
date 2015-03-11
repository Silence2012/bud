import json
from flask import Flask
import sys
sys.path.append('../')
from agent.handle import Handle
from agent.container import Container
app = Flask(__name__)
@app.route("/")
def getData():
    handle = Handle()
    ret = json.dumps(handle.getMetric())
    return ret
