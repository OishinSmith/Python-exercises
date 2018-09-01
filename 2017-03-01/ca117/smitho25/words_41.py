import sys
import string
lines = sys.stdin.read().strip().split()


d = {}
for word in lines:
  word = word.lower().replace(string.punctuation, "")
  for letter in word:
    if letter in string.punctuation and letter != "'":
      word = word.replace(letter, "")
  if not word:
    continue
  elif word not in d:
    d[word] = 1
  else:
    d[word] = d[word] + 1


for (k, v) in sorted(d.items()):
  print("{} : {}".format(k , v))
