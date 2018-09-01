import sys
line = sys.stdin.readlines()

d = {}
e = []
for word in line:
  team_name = " ".join((word.strip().split())[:-5])
  score = " ".join((word.strip().split())[-5:])
  total_score = 0
  new_score = ""
  for number in score.split():
    if number in "0123456789":
      new_score = new_score + str(number)
  if len(new_score) == 5:
    for number in new_score:
      total_score = total_score + int(number)
    d[team_name] = total_score

def sorter(t):
  return t[1]
  d = {} 
f = []
max_len = 0
for length in d.keys():
  if len(length) > max_len:
    max_len = len(length)

max_len2 = 0
for length in d.values():
  if len(str(length)) > max_len2:
    max_len2 = len(str(length))

for k, v in sorted(d.items(), key = sorter, reverse = True):
  print("{:>{}} {:>{}} points".format(k, max_len, v, max_len2))
