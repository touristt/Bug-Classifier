from flask import Flask, request, jsonify, render_template
import json
import numpy as np
from Perceptron import *
from Bug import Bug
from flask_cors import CORS

W,B = train()

app = Flask(__name__)

CORS(app)

@app.route("/", methods=['GET','POST'])
def getfunc(): 

	if request.method == "GET":
		return render_template('index.html')

	datum = request.get_json()
	return Check(Bug(datum['length'],datum['width']),W,B)

if __name__ == '__main__':
		app.debug = True
		app.run(host="0.0.0.0", port=5000)