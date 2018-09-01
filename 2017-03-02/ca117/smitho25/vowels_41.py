import sys
import string
lines = sys.stdin.read().strip().split()

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"

d = {}
for word in lines:
  word = word.lower().replace(string.punctuation, "")
  for letter in word:
    if letter in string.punctuation and letter != "'":
      word = word.replace(letter, "")
  for letter in word:
    if letter not in d:
      d[letter] = 1
    else:
      d[letter] = d[letter] + 1

max_width = len(str(max(d.values())))

for (k, v) in sorted(d.items(), key = lambda d: d[1], reverse = True):
  if k in "aeiou":
    print("{:>s} : {:>{:d}d}".format(k, v, max_width))



"""
new_dict = [] #for words
num_list = [] #for numbers
for (k, v) in sorted(d.items()):
  if v >= 3 and len(k) > 3:
    new_dict.append(k)

for (k, v) in sorted(d.items()):
  if v >= 3 and len(k) > 3:
    num_list.append(v)

max_length = 0
for word in new_dict:
  if len(word) > max_length:
    max_length = len(word)

max_num_len = 0
for number in num_list:
  if len(str(number)) > max_num_len:
    max_num_len = len(str(number)) 

for (k, v) in sorted(d.items()):
  if v >= 3 and len(k) > 3:
    print("{:>{:d}s} : {:>{:d}d}".format(k, max_length, v, max_num_len))
"""
