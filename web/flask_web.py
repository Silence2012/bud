import json
from flask import Flask
import sys
sys.path.append('../')
from handle import Handle
from container import Container
app = Flask(__name__)
@app.route("/")
def getData():
    handle = Handle()
    ret = json.dumps(handle.getMetric())
    return ret
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8888,debug=True)
