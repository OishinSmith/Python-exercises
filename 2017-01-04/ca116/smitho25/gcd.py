olda = input()
oldb = input()
while oldb != 0:
  newa = oldb
  newb = olda % oldb
  olda = newa
  oldb = newb
print olda
