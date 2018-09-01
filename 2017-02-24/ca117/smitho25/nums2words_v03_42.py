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
mapp = sys.argv[1]

d = {}

with open(mapp, "r") as f:
  for word in f:
    word = word.strip().split()
    d[word[0]] = word[1]


for line in lines:
  line = line.strip().split()
  i = 0
  sentence = ""
  while i < len(line):
    if line[i] in numbers:
      tran_num = numbers[line[i]]
      sentence = sentence + " " + d[tran_num]
  
    #else:
      #line[i] = ("unknown") 
    i += 1
  print(sentence.strip())



