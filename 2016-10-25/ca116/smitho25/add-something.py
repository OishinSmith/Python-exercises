a = []

line = raw_input()
while line != "end":
  a.append(int(line))
  line = raw_input()

n = input()
i = 0
while i < len(a):
  print a[i] + n

  i = i + 1

