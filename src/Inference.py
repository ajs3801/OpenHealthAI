import warnings
import sys
import pandas as pd
import pickle
def PreProcessToList(coordinate_str):
  string_list = coordinate_str.split(',')

  for i in range(len(string_list)):
    string_list[i] = float(string_list[i])

  return string_list

def Inference(coordinate_list):
  with open("../model/ActionV7.pkl", 'rb') as f:
    model = pickle.load(f)

  with warnings.catch_warnings():
      warnings.simplefilter("ignore")
      # coordinate inference
      X = pd.DataFrame([coordinate_list])
      current_class = model.predict(X)[0]
      current_class_prob = model.predict_proba(X)[0]

      return current_class

if __name__ == '__main__':
  coordinate_str = sys.argv[1]
  coordinate_list = PreProcessToList(coordinate_str)
  print(Inference(coordinate_list))
  
# print("#LENGTH  : {}".format(len(squat_list)))
# print("#ANSWER  : squat")
# print("#PREDICT : {}".format(Inference(squat_list)))