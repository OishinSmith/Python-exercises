german_words = {
  "one": "einz",
  "two": "zwei",
  "three": "drei",
  "four": "vier",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn", 
 
}

import sys 
lines = sys.stdin.read().split()
for words in lines:
   if words in german_words:
     print german_words[words]
