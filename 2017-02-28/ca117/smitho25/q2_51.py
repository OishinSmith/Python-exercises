import sys
line = sys.stdin
a = []
for word in line:
  checker_string = ""
  word = word.strip()
  for char in word.lower():
     if char in "evil":
        checker_string += char
  if checker_string == "evil":
     print(word)


