import sys
lines = sys.stdin.readlines()

i = 0
total = 0
while i < len(lines):
  total = total + int(lines[i])
  i += 1
sys.stdout.write(str(total) + "\n") 


