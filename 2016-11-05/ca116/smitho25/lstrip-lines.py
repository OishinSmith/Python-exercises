n = raw_input()

while n != "end":
  i = 0
  while i < len(n) and n[i] == " ":
    i = i + 1
  print n[i:]        #you have to put this ouside the loop, or it'll loop i < len(n) times
  n = raw_input()
   
