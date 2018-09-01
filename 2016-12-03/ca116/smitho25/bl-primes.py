import sys
numbers = int(sys.argv[1])
a = []

i = 2
while i < numbers:
  true = True
  j = 2
  while j < i:
    if i % j == 0:
      true = False
    j = j + 1

  if i % j == 0 and true:
    a.append(i)
  i = i + 1

for number in a:
  print number




"""
i = 1
a = []

j = 1
true = True
while i < numbers:
  while j < i:
    if i % j != 0:
      true == True
    j = j + 1

  if i % j == 0 and i % i == 0 and j % j == 0:
    a.append(i)
  i = i + 1
print a

# only prints the numbers from 1 - 19 and not working, need to add
i < j

  


"""


"""

  j = 2
  t = True
  while j != i:
    if i % j != 0:
      t == True
    j = j + 1
    if i % j == 0 and i % i == 0 and j % j == 0:
      print i
    i = i + 1
# doesnt work
"""
