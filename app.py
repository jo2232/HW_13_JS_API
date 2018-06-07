# import necessary libraries
import numpy as np
import os
import csv
import pandas as pd
import bellybutton
import json
from flask_cors import CORS

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)
CORS(app)
# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Query the database and send the jsonified results
# @TODO: Create a route to accept your form data and
# save it to your database
@app.route("/names")
def names():
    bellybutton.samples()
    with open('sample_names.txt') as json_file:  
        data = json.load(json_file)
    return jsonify(data)

@app.route("/otu")
def otu():
    bellybutton.otuList()
    with open('bellybutton_taxo_otu.txt') as json_file:  
        data = json.load(json_file)
    return jsonify(data)

@app.route("/metadata/<sample>", methods=['POST'])
def metadata(sample):
    sample_id = sample
    bellybutton.meta(sample_id)
    with open('bellybutton_metadata.txt') as json_file:  
        data = json.load(json_file)
    return jsonify(data)

@app.route("/wfreq/<sample>")
def wfreq(sample):
    sample_id = sample
    bellybutton.wfreq(sample_id)
    with open('bellybutton_wfreq.txt') as json_file:  
        data = json.load(json_file)
    return jsonify(data)

@app.route("/samples/<sample>", methods=['GET','POST'])
def sample_values(sample):
    sample_id = sample
    bellybutton.otuValues(sample_id)
    with open('bellybutton_otu_samples.txt') as json_file:  
        data = json.load(json_file)
    return jsonify(data)
# @TODO: Create a route to send the data needed for your plots

if __name__ == "__main__":
    app.run()
