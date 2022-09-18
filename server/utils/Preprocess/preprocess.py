def PreProcessToList(coordinate_str):
  coordinate_str = str(coordinate_str)
  coordinate_str.strip()
  print(coordinate_str)
  string_list = coordinate_str.split(' ')

  print('length' , len(string_list))
  
  del string_list[0]

  for i in range(len(string_list)):
    string_list[i] = float(string_list[i])
    
  return string_list