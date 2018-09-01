import sys
import string
lines = sys.stdin.readlines()

for sentence in lines:

  seen = []
  count = 0
  for word in sentence:
    if string.digits not in seen and word in string.digits:
      count = count + 1
      seen.append(string.digits)
    elif string.ascii_uppercase not in seen and word in string.ascii_uppercase:
      count = count + 1
      seen.append(string.ascii_uppercase)
    elif string.punctuation not in seen and word in string.punctuation:
      count = count + 1
      seen.append(string.punctuation)
    elif string.ascii_lowercase not in seen and word in string.ascii_lowercase:
      count = count + 1
      seen.append(string.ascii_lowercase)
  print(count)
  
