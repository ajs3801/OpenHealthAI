import pickle
import pandas as pd
import warnings

def Inference(coordinate_list):
  with open("../model/ActionWV1.pkl", 'rb') as f:
    model = pickle.load(f)

  with warnings.catch_warnings():
      warnings.simplefilter("ignore")
      # coordinate inference
      X = pd.DataFrame([coordinate_list])
      current_class = model.predict(X)[0]
      current_class_prob = model.predict_proba(X)[0]

      return current_class