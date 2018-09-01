import sys
number = sys.argv[1]

x = 1
i = 0
while i < len(number):
  x = x * int(number[i])
  i = i + 1
print x
