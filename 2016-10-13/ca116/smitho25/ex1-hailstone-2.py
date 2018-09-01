n = input()
i = 0
print n
while i < 4:
  if n % 2 == 0:
    n = n / 2     
  else:
    n = n * 3 + 1
  print n
  i = i + 1
