import sys
lines = sys.stdin.readlines()
list_a = []
vowels = "aeiou"

for n in lines:
  n_removed = n.replace("\n", "")
  list_a.append(n_removed)

print([word for word in list_a if len(word) == 17])

print([word for word in list_a if len(word) > 17])

print(min([word for word in list_a if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower()], key = len))

print(


