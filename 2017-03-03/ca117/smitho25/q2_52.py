import sys
line = sys.stdin.read()

d = {}
e = []
for word in line:
  word = word.strip()
  if word not in d:
    d[word] = 1
    e.append(word)
  else:
    d[word] = d[word] + 1

for c in e:
  if d[c] == 1:
    print(c)
