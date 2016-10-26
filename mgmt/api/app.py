from flask import Flask, json

from utils import util

app = Flask(__name__)

@app.route("/service_list")
def service_list():
    return None

@app.route("/jenkins/status")
def verify_jenkins():
    return None

@app.route("/services/start/<service_name>")
def start_service(service_name):
    return "%s started" % service_name

@app.route("/services/stop/<service_name>")
def stop_service(service_name):
    return "%s stopped" % service_name

def find_dependent_service_list(service_name):
    return None

@app.route("/services/status/<service_name>")
def service_status(service_name):
    return "%s status" % service_name