a = []
n = raw_input()
avarage = 0.0

while n != "end":
  a.append(float(n))
  avarage = avarage + float(n)
  n = raw_input()

if len(a) != 0:
  avarage = avarage / len(a)

i = 0
while i < len(a):
  if float(a[i]) > avarage:
    print int(a[i])
  i = i + 1
