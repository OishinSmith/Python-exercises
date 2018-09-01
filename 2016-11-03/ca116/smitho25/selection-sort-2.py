s = raw_input()

a = []

while s != "end":
  a.append(int(s))
  s = raw_input()
n = input()
i = n
p = n
while i < len(a):
  if a[i] < a[p]:
    p = i
  i = i + 1
print p
