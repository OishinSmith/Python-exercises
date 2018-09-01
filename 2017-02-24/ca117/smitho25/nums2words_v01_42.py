import sys
lines = sys.stdin.readlines()

numbers = {
  "0" : "zero",
  "1" : "one",
  "2" : "two",
  "3" : "three",
  "4" : "four",
  "5" : "five",
  "6" : "six",
  "7" : "seven",
  "8" : "eight",
  "9" : "nine",
  "10" : "ten",
}

for line in lines:
  line = line.strip().split()
  i = 0
  while i < len(line):
    if line[i] in numbers:
       line[i] = numbers[line[i]]
    i += 1
  print(" ".join(line))
