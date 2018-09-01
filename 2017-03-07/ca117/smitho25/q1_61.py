import sys
line = sys.argv[1]

i = 0
if len(line) % 2 == 0:
  string = ""
  while i < len(line) - 1:
    tmp = line[i]
    value1 = line[i + 1]
    value2 = tmp
    value3 = value1 + value2
    string = string + value3
    i = i + 2
  print(string)
    
else:
  string = ""
  while i < len(line) - 1:
    tmp = line[i]
    value1 = line[i + 1]
    value2 = tmp
    value3 = value1 + value2
    string = string + value3
    i = i + 2
  print(string + line[-1])
    
