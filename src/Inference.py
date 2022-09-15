import warnings
import sys
import pandas as pd
import pickle
import torch
# javscript에서 list 자료구조로 바로 sys argument로 보내주는 것이 없으므로, string으로 보내줄 수 밖에 없음
# 이때, input string list에서 , 기준으로 끊고 float 형식으로 바꿔줌
def PreProcessToList(coordinate_str):
  string_list = coordinate_str.split(' ')

  for i in range(len(string_list)):
    string_list[i] = float(string_list[i])

  return string_list

# Inference모델로 받은 input으로 model/ActionV7.pkl을 돌려서 결과 Return
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

# javascript에서 python 파일을 실행할 때 실행되는 로직순서
if __name__ == '__main__':
  coordinate_str = sys.argv[1] # sys.argv[1] : javascript의 첫번째 argument
  coordinate_list = PreProcessToList(coordinate_str)
  print(Inference(coordinate_list)) # 모델 결과 출력