import sys

sentence = sys.stdin.readlines()

i = 0
while i < len(sentence):
  split_sentence = (sentence[i][0:len(sentence[i])-1]).split(" ")
  print(" ".join(word[0:len(word) - 1] + word[-1].upper() for word in split_sentence))
  i = i + 1

"""
lines = sys.stdin.readlines()
print(lines)
i = 0
while i < len(lines): #cycles through lines
  j = 0
  words = lines[i].replace("\n", " ").split(" ")
  
  " ".join(letters[-1].upper() for letters in split_sentence)
  

  print(words[0:len(words)-1]) #print((lines[i])[j]) prints vertically
  i = i + 1

    
  


sentence = sys.stdin.readlines()
i = 0
while i < len(sentence):
  split_sentence = sentence[i].replace("\n", " ").split(" ")
  print(split_sentence)
  capitalized = " ".join([word[0:len(word) - 1] + word[-1].upper() for word in split_sentence])
  sys.stdout.write((capitalized))
  i = i + 1
"""


