import sys
for line in sys.stdin:
  is_anagram = True
  two_words = line.split()
  for char in two_words[0]:
    if char in two_words[1]:
      two_words[1] = two_words[1].replace(char,'',1)
    else:
      is_anagram = False
  if two_words[1] != '':
      is_anagram = False
  print(is_anagram)

