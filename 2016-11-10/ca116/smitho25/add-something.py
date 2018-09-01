"""a = []

line = raw_input()
while line != "end":
  a.append(int(line))
  line = raw_input()

n = input()
i = 0
while i < len(a):
  print a[i] + n

  i = i + 1""" #method one

a = []
n = raw_input()
while n != "end":
  a.append(int(n))
  n = raw_input() #list done
 
s = " "
n = input()
i = 0
while i < len(a):
  s = a[i] + n
  print s
  i = i + 1

