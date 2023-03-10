import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(autoload_with = engine)

app = Flask(__name__)

@app.route('/')
def homepage():
    return(
        f"Welcome to my Honolulu Precipiation API! <br/>"
        f"Here are the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> (Input a start date YYY-MM-DD)<br/>"
        f"/api/v1.0/<start>/<end> (Input start and end dates)"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    return()

@app.route('/api/v1.0/stations')
def stations():
    return()

@app.route('/api/v1.0/tobs')
def tobs():
    return()

@app.route('/api/v1.0/<start>')
def startdate():
    return()

@app.route('/api/v1.0/<start>/<end>')
def startenddate():
    return()

if __name__ == '__main__':
    app.run(debug=True)