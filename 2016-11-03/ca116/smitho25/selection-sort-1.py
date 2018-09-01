s = raw_input()

a = []

while s != "end":
  a.append(int(s))
  s = raw_input()
i = 0
p = 0
while i < len(a):
  if a[i] < a[p]:
    p = i
  i = i + 1
print p
