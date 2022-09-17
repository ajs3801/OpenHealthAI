def PreProcessToList(coordinate_str):
  coordinate_str = str(coordinate_str)
  string_list = coordinate_str.split(',')

  for i in range(len(string_list)):
    string_list[i] = float(string_list[i])

  return string_list