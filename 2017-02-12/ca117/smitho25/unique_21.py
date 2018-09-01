import sys
import string

lines = sys.stdin.read().split()
a = []

for words in lines:
  for letter in words:
    if not letter.isalnum():
      words = words.replace(letter, "")
  words = words.lower() 
 
  if words not in a:
    a.append(words)
  
print(len(a) - 1) #Potatoes
