import sys
import string

for line in sys.stdin:
  line = line.strip().lower()
  for char in line:
    if not char.isalnum():
      line = line.replace(char,'')
  if line[::-1] == line:
    print(True)
  else:
    print(False)

