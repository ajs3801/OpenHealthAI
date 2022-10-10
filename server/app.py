# import ML library
import utils.Inference as I
import utils.Preprocess as P
import utils.Print as Print
# for server
from flask import Flask, request, render_template, jsonify
import json

# for ML
import pandas as pd
import pickle
import warnings

# Declare a Flask app
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def connect():
  print('connect')
  if request.method == 'POST':
    value_json = request.get_json()
    value = value_json['data']

    with warnings.catch_warnings():
      warnings.simplefilter("ignore")
      value = P.PreProcessToList(value)
      Inference_value = I.Inference(value)

    Print.PostResult(value,Inference_value)

    return jsonify(result = "success", result2= Inference_value)

  else:
    return render_template('pose.html')

# Running the app
if __name__ == '__main__':
  app.run('0.0.0.0',port=8000,debug = True)