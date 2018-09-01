import sys
line = sys.argv[1]

if len(line) % 2 == 0:
  print("No middle character!")
else:
  print(line[int((len(line) / 2) - 0.5)])
