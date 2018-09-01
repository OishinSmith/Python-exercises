import sys
d = {} # a simple way to stop a l
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
  split_lines = lines[i].split()
  user_name = split_lines[3]


  if i != 1000:
    d[user_name] = " user-" + str(i + 1) + " "
    i = i + 1

  split_lines[3] = d[user_name]
  split_lines = "".join(split_lines)
  i = i + 1
  print split_lines


"""
import sys

lines = sys.stdin.readlines()
print lines
a = []
split_lines = []
i = 
while i < len(lines):
  a.append(lines)
  print a
  split_lines = lines[i].split()
  user = a[3]
  i = i + 1
print split_lines
"""
"""import sys
pattern = sys.stdin.
replacement = sys.argv[2]

line = raw_input()
while line != "end":
  i = 0
  while i < len(line) and line[i:i + len(pattern)] != pattern:
    i = i + 1

  if i < len(line):
    print line[0:i] + replacement + line[i + len(pattern):]
  else:
    print line
  line = raw_input()
"""
"""
import sys

sentence = raw_input()
print sentence
while sentence != "end":
  i = 0
  
  word_to_be_replaced = sentence[3]
  while i < len(sentence) and sentence[i:i + len(word_to_be_replaced)] != word_to_be_replaced:
    i = i + 1
  replacement = "user", (i + 1)
  if i < len(sentence):
    print sentence[0:i] + replacement + sentence[i + len(word_to_be_replaced):]
  else:
    print sentence
  sentence = raw_input()
"""
