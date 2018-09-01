n = input()
prev = 1
curr = 1
i = 0
while n > prev:
  print prev
  curr = prev + curr
  prev = curr-prev
  i = i + 1