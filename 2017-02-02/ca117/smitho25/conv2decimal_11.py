
"""
import sys
def decimal(num, base):
  total = 0
  power = 0
  for c in num[::-1]:
    total = (int(c) * (int(base) ** int(power))
    power = power + 1
  return total
print(decimal(sys.argv[1], sys.argv[2]))
"""



import sys
binary = sys.argv[1]
base = sys.argv[2]

power = 0
total = 0
for c in binary[::-1]:
  total = total + (int(c) * (int(base) ** int(power)))
  power = power + 1
print(total)

    
    
