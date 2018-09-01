import sys
lines = sys.stdin.readlines()

es = ("ch", "sh", "x", "s", "z")
ves = ("f", "fe")
vowels = ("a", "e", "i", "o", "u")
oes = ("o")
# consonants = the inverse of vowels

for sentence in lines:
  sentence = sentence.strip()
  if sentence[-2:] in es or sentence[-1] in es:
    print(sentence + "es")
  elif sentence[-1] in oes:
    print(sentence + "es")
  elif sentence[-1] == "y" and sentence[-2] not in vowels:
    print(sentence[:len(sentence) - 1] + "ies")
  elif sentence[-2:] == "fe":
    print(sentence[:len(sentence) - 2] + "ves")
  elif sentence[-1] == "f":
    print(sentence[:len(sentence) - 1] + "ves")
  else:
    print(sentence + "s")
  













"""
  print(sentence[-1])
  for endings in es:
    if (sentence[len(sentence)-3:len(sentence)-1]) == endings:
      print("yeah")
  for endings in es_single:
    if (sentence[-1]):
      print("yeah")
"""
