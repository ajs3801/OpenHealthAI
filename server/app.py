import utils.Inference as I
import utils.Preprocess as P

from flask import Flask, request, render_template
import pandas as pd
import pickle
import warnings
import json

# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------
@app.route('/', methods=['GET', 'POST'])
def main():
    # If a form is submitted
    if request.method == "POST":
      # Unpickle classifier
      with open("../model/ActionV7.pkl", 'rb') as f:
        model = pickle.load(f)

      with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Get values through input bars
        coordinate_list = request.form.get("coordinate_list")
        print(coordinate_list)

        coordinate_list = P.PreProcessToList(coordinate_list)
        current_class = I.Inference(coordinate_list)

    else:
      current_class = "Input"
    
    print('up')
    return render_template("test.html", output = current_class)

@app.route('/test', methods=['POST'])
def test():
  output = request.get_json()
  result = json.loads(output) #this converts the json output to a python dictionary

  coordinate_list = result['']
  print(result)

  if request.method == "POST":
    coordinate_list = P.PreProcessToList(coordinate_list)
    current_class = I.Inference(coordinate_list)

  else:
    current_class = "Input"

  print('down')
  return render_template("test.html", output = current_class)
# Running the app
if __name__ == '__main__':
  app.run('0.0.0.0',port=8000,debug = True)