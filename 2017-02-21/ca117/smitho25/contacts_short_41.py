import sys
lines = sys.argv[1]
d = {}
with open(lines) as f:
  details = f.readlines()
  for sentences in details:
    sentences = sentences.strip().split(" ")
    #print(sentences)
    name = sentences[0]
    number = sentences[1]
    d[name] = number
    
lines_2 = sys.stdin.readlines()
for words in lines_2:
  name = words.strip() 
  if name in d.keys():
    print("Name:", name)
    print("Phone:", d[name])
  else:
    print("Name:", name)
    print("No such contact")


