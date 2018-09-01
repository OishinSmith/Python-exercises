import sys
line = sys.argv[1]
if len(line) > 1:
  print(line[0].upper() + line[1:-1] + line[-1].upper())

  
