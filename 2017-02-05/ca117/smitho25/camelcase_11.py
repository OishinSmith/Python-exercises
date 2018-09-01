import sys
sentence = sys.stdin.readlines()

i = 0
while i < len(sentence):
  split_sentence = sentence[i].split(" ")
  capitalized = " ".join(word.capitalize() for word in split_sentence)
  sys.stdout.write((capitalized))
  i = i + 1
"""
i = 0
while i < len(sentence):
  sys.stdout.write((sentence[i]).title())
  i = i + 1


============
print(sentence)

i = 0
while i < len(sentence):
  split_sentence = sentence[i].split(" ")
  print(split_sentence)
  for word in split_sentence:
    capitalized = word.capitalize()
    print(capitalized)
  i = i + 1
"""
