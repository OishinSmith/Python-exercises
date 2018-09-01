n = raw_input()

while n != "end":
  x = 1
  i = 0
  while i < len(n):
    x = x * int(n[i])
    i = i + 1
  print x
  n = raw_input()

