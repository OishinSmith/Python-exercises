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
    e_mail = sentences[2]
    d[name] = number, e_mail

with open(lines) as f:
  details = f.readlines()
  for sentences in details:
    sentences = sentences.strip().split(" ")
    
    
lines_2 = sys.stdin.readlines()
for words in lines_2:
  name = words.strip() 
  if name in d.keys():
    print("Name:", name)
    print("Phone:", d[name][0])
    print("Email:", d[name][1])
  else:
    print("Name:", name)
    print("No such contact")
