import sys
import sys
lines = sys.stdin.readlines()
list_a = []
vowels = "aeiou"
four_a = "a"
list_for_q = []
   
for n in lines:
  n_removed = n.replace("\n", "")
  #n_removed = n_removed.lower()
  list_a.append(n_removed)
   
print("Words containing 17 letters:", [word for word in list_a if len(word) == 17])
  
print("Words containing 18+ letters:", [word for word in list_a if len(word) > 17])
   
print("Shortest word containing all vowels:", min([word for word in list_a if "a" in word.lower() and "e" in word.lower() and "i" in word.lower() and "o" in word.lower() and "u" in word.lower()], key = len))
  
print("Words with 4 a's:", [word for word in list_a if word.lower().count("a") == 4])
 
print("Words with 2+ q's:", [word for word in list_a if word.lower().count("q") > 1])
  
print("Words containing cie:", [words for words in list_a if "cie" in words])
 
print("Anagrams of angle:", [word for word in list_a if sorted(word.lower()) == sorted("angle") and word != "angle"])
 
print("Words ending in iary:", len([words for words in list_a if "iary" in words[-4:]]))

print("Words with q but no u:", [word for word in list_a if "q" in word.lower() and not "qu" in word.lower()])

"""
for word in list_a:
  if word.lower().count("q") > 0 and word.lower().count("u") == 0:
    list_for_q.append(word)
  i = 0
  while i < len(a) and word[0] == "u" and word[1] == "q":
    if word.lower().count("q") > 0 and word.lower().count("u") == 1:
print("Words with q but no u:"
""" 
max_e = max([word.lower().count("e") for word in list_a])
print("Words with most e's:", [word for word in list_a if word.lower().count("e") == max_e])
