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

# @app.route('/', methods=['GET', 'POST'])
# def main():
#     try:
#       # If a form is submitted
#       if request.method == "POST":
#         # # Unpickle classifier
#         # with open("../model/ActionV7.pkl", 'rb') as f:
#         #   model = pickle.load(f)

#         # with warnings.catch_warnings():
#         #   warnings.simplefilter("ignore")
#         #   # Get values through input bars
#         #   coordinate_list = request.form.get("coordinate_list")
#         #   print(coordinate_list)
#         coordinate_list = P.PreProcessToList(coordinate_list)
#         current_class = I.Inference(coordinate_list)

#       else:
#         current_class = "Input"
      
#       print('up')

#       return render_template("test.html", output = current_class)
#     except:
#       print('SERVER ERROR')

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