from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_client import Counter, generate_latest
import socket

app = Flask(__name__)
CORS(app)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

@app.route("/")
def home():

    REQUEST_COUNT.inc()

    return jsonify({

        "Application":"Backend API",

        "Status":"Running",

        "Hostname":socket.gethostname()

    })

@app.route("/health")
def health():

    REQUEST_COUNT.inc()

    return jsonify({

        "status":"Healthy"

    })

@app.route("/version")
def version():

    REQUEST_COUNT.inc()

    return jsonify({

        "version":"1.0.0"

    })

@app.route("/info")
def info():

    REQUEST_COUNT.inc()

    return jsonify({

        "Owner":"Manoj Kumar",

        "Platform":"AKS",

        "Environment":"Development"

    })

@app.route("/metrics")
def metrics():

    return generate_latest(),200,{
        "Content-Type":"text/plain"
    }

if __name__=="__main__":

    app.run(host="0.0.0.0",port=5000)