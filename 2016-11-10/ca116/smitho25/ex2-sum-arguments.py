import sys
integers = sys.argv[1]
n = 0
i = 0
while i < len(integers):
  n = n + int(integers[i])
  i = i + 1
  
print n


