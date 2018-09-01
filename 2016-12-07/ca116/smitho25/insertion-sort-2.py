a = []
s = raw_input()

while s != "end":
  a.append(int(s))
  s = raw_input()

n = input()
a.append(n)
position = len(a)-1
while position > 0 and n < a[position - 1]:
  a[position] = a[position - 1]
  position = position - 1
  a[position] = n
print a

