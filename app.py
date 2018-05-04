from flask import Flask
from flask import json
import time
import datetime

app = Flask(__name__)

@app.route("/")
def getTimestamp():
    data = {"time" : ""}
    ts = time.time()
    data["time"] = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
   
