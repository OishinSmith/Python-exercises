a = []
b = []


line = raw_input()
while line != "end":
  a.append(int(line))
  line = raw_input()


line = raw_input()
while line != "end":
  b.append(int(line))
  line = raw_input()

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
      print a[i]
      i = i + 1
    else:
      print b[j]
      j = j + 1

while i < len(a):
  print a[i]
  i = i + 1

while j < len(b):
  print b[j]
  j = j + 1


