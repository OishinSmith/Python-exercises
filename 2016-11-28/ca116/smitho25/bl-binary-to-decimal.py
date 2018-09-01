import sys
binary = sys.argv[1]

bina = ""

for c in binary:
  bina = c + bina  

i = 0
decimal = 0
while i < len(bina):
  decimal = decimal + (int(bina[i]) * (2 ** i))
  i = i + 1 
  
print decimal
