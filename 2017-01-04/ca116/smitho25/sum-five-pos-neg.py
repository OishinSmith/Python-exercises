i = 0
p = 0
m = 0 #negative
while i < 5:
  n = input()
  if n >= 0: #positive
    p = n + p
  else:
    n = n * -1
    m = n + m
  i = i + 1
print (m * -1), p
  
