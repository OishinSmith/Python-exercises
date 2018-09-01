import sys
lines = sys.stdin
digits = "1234567890"
i = 0

for letters in lines:
  letters = letters.strip()
  if letters[i] not in digits:
    print(letters, "is not a number")
  else:
    print("Thank you for", letters)
    sys.exit()

"""
#if not letters.isdigit():

import sys
line = sys.stdin.readlines()
numbers = "1234567890"
for sentences in line:
  sentences.strip().split()
  is_number = True
  for letters in sentences:
    if letters in numbers:
      is_number = True
      print("Thank you for", sentences)
      sys.exit()
  else:
    print(sentences, "is not a number")
"""
