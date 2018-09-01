i = 0
p = 0
m = 0 #negative
n = ""
while n != 0:
  n = input()
  if n >= 0: #positive
    p = n + p
  else:
    n = n * -1
    m = n + m
print (m * -1), p


  
