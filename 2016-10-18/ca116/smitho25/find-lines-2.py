import sys
pattern = sys.argv[1]

line = raw_input()
while line != "end":
  i = 0
  while i < len(line) and line[i:i + len(pattern)] != pattern: #len is the ammount of characters in a "string"
    i = i + 1
  if i < len(line):
    print i
  else:
    print "-1"
    
  line = raw_input()
