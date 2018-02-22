from flask import Flask, request, render_template, redirect, send_from_directory
from DBManager import *
from json import dumps
import argparse

parser = argparse.ArgumentParser(description='Runs a system which handles appointments.')
parser.add_argument('-H', '--host', type=str, default='localhost',
                    help='The hostname to access this. To make public use 0.0.0.0. Default: \'localhost\'')
parser.add_argument('-p', '--port', type=int,
                    default=80, help='The port number. Use 80 for the browser default. Default: 80')
parser.add_argument('-d', '--dbfile', type=str,
                    default=':memory:', help='The name of the file the database uses. Default: \':memory:\'')
args = parser.parse_args()

app = Flask(__name__, static_url_path='')

dbm = DBManager(args.dbfile)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search_appointments():
    if len(request.args) != 1:
        return dumps(dbm.present_appointments())
    query = request.args["query"]
    return dumps(dbm.present_appointments(query))

@app.route("/new")
def create_appointment():
    date = request.args.get("date")
    time = request.args.get("time")
    description = request.args.get("description")
    dbm.add_appointment_to_db(date, time, description)
    return redirect('/')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

app.run(args.host, args.port)
