import sys
with open("translation.txt") as a:
  a = a.readlines()
i = 0
while i < len(a):
  line = a[i].split()
  i = i + 1
  print line[0]



d = {
  "one": "eins",
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



