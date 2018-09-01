'''import sys
pattern = sys.argv[1]

line = raw_input()
while line != "end":
  i = 0
  while i < len(line) and line[i:i + len(pattern)] != pattern:
    i = i + 1
  if i < len(line):
    print "yes"
  else: 
    print "no"
  line = raw_input()'''
import sys
pattern = sys.argv[1]

s = raw_input()
while s != "end":
  i = 0
  while i < len(s):
    if s[i:i + pattern] == pattern
      print "yes"
    else:
      print "nein"
