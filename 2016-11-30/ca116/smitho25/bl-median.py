a = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

i = 0
if len(a) / 2:
  print a[len(a) / 2]
  

"""

s = raw_input()
while s != "end":
  a.append(int(s))
  i = 0
  j = i + 1
  
while i < len(a):
  if a[i] < a[j]:
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    i = i + 1
    s = raw_input()
print a
"""

