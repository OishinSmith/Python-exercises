"""a = []
s = raw_input()

while s != "end":
  a.append(int(s))
  s = raw_input()
  
n = input()
p = len(a)
while p > 0 and a[p - 1] > n:
  p = p - 1
  
print p"""
a = []
s = raw_input()

while s != "end":
  a.append(int(s))
  s = raw_input()
  
n = input()
p = 0
i = 0
while i < len(a):
  if a[i] <= n:
    p = p + 1
  i = i + 1
print p
  
  


  
    
