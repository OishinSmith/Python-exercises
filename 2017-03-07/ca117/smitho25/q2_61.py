import sys
line = sys.stdin.read().split()

a = []
for word in line:
  if "@" in word:
    name = word.split("@")
    a.append(name[0])

for name_sur in a: 
  name_sur = name_sur.split(".")
  print(name_sur[0].capitalize(), name_sur[1].capitalize())
