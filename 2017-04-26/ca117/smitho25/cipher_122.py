import sys
paragraph = sys.stdin.read()
d = {
"A" : 1,
"B" : 2,
"C" : 3,
"D" : 4,
"E" : 5,
"F" : 6,
"G" : 7,
"H" : 8,
"I" : 9,
"J" : 10,
"K" : 11,
"L" : 12,
"M" : 13,
"N" : 14,
"O" : 15,
"P" : 16,
"Q" : 17,
"R" : 18,
"S" : 19,
"T" : 20,
"U" : 21,
"V" : 22,
"W" : 23,
"X" : 24,
"Y" : 25,
"Z" : 26,
"0" : 27,
"1" : 28,
"2" : 29,
"3" : 30,
"4" : 31,
"5" : 32,
"6" : 33,
"7" : 34,
"8" : 35,
"9" : 36,
} 

d2 = {
1:"A",
2:"B",
3:"C",
4:"D",
5:"E",
6:"F",
7:"G",
8:"H",
9:"I",
10:"J",
11:"K",
12:"L",
13:"M",
14:"N",
15:"O",
16:"P",
17:"Q",
18:"R",
19:"S",
20:"T",
21:"U",
22:"V",
23:"W",
24:"X",
25:"Y",
26:"Z",
27:"0",
28:"1",
29:"2",
30:"3",
31:"4",
32:"5",
33:"6",
34:"7",
35:"8",
36:"9",
} 

 

words = {
  "a"
  "i"
  "am"
  "be"
  "in"
  "to"
}

d2 = {}

for word in paragraph:
  word = word.strip().split()
  for letter in word:
    #print(letter)
    if letter in d2:
      #print(letter)
      d2[letter] = d2[letter] + 1
    else:
      d2[letter] = 1

#you need the max number of occurances for a specific character or this will not work. I had it going to A before, but it didnt work at all
number_occurances = (max(d2.keys(), key = lambda x:d2[x]))#a or e
#print(number_occurances)
shiftkey = (36 - (d[number_occurances] - 5)) #if J is the max value, d[J] = 10. therefore 36 - (10 - 5) = 31.
list_all = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

list_b = []
for letter in paragraph:
  #print(letter)
  if letter.isalnum():
    if letter in d:
      #if its a letter or number do this
      list_b.append(list_all[((d[letter] - 1)+ shiftkey) % len(d)])
  else:
    list_b.append(letter)
print("".join(list_b).strip())
"""
b = []
for letter in paragraph:
  #print(letter)
  if letter.isalnum():
    if letter in d:
      #print(a.index(letter), d[letter] - 1)
      b.append(a[((d[letter] - 1)+ shiftkey) % len(d)])
  else:
    b.append(letter)
print("".join(b).strip())
---------------------------------------
for word in paragraph:
  word = word.strip(",.;:")
  i = 0
  if len(word) == 1:
    position = d[word]
    string = "abdefghijklmnopqrstuvwxyz0123456789"
    shift = position - (position - 1)
    #shift = (string[shift - 1])
  
for word in paragraph:
  for letter in word:
    string = "abdefghijklmnopqrstuvwxyz0123456789"
    if letter in d:
      print(string[d[letter] - 2 + shift])
"""
