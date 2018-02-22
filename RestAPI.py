from flask import Flask, request, render_template, redirect, send_from_directory
from DBManager import *
from json import dumps

app = Flask(__name__, static_url_path='')

dbm = DBManager()

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

app.run('localhost', 80)