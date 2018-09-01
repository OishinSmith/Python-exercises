prev = input()
cur = input()
while cur != 0:
  if prev < cur:
  	print "higher"
  elif prev == cur:
  	print "equal" 
  else:
  	print "lower"
  prev = cur
  cur = input()