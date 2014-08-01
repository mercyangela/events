import os
import json
import urllib.request
from flask import Flask, request, g, redirect, abort, \
     render_template, flash

#Create application
app = Flask(__name__)
app.config.from_object(__name__)

def load_events():
    json_data = urllib.request.urlopen("http://kolastudios.com/internship/ester/get_events.php").readall().decode('utf-8')
    data = json.loads(json_data)
    return data['events']

@app.route('/')
def show_entries():
    entries = load_events()
    return render_template('show_entries.html', entries=entries)

@app.route('/details/')
def details():
    entries = load_events()
    e = {"Name":"None", "Content":"None", "Location":"None"}
    for event in entries:
        if event["event_id"] == request.args["event_id"]:
            e = event
    return render_template('show_details.html', entry=e)

if __name__=="__main__":
    app.run()
