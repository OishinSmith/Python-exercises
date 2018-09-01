import sys
from copy import deepcopy, copy
#bggest program ever, dont judge. I hope it works. ps. it was purposely designed to be long and complicated.

def horizontal(size, x_and_dots):
  count = 0 #return the total amount of occurances
  c = []
  for value in x_and_dots.split("."):
    if "x" in value:
      c.append(value)
  for x in c:
    #print(x) will give you the list of X's
    if int(1 * size) == len(x):
      count = count + 1
  return count

def vertical(lista, size):
  
  i = 0
  vertical = []
  types = []
  while i < len(lista):
    numlist = lista[i]
    list_copy = copy(lista)
    for number in numlist:
      count = 1 #has to start at one due to the question
      j = i + 1
      #print(j, "j value", number, "number in", list_copy[j], "lisst copy[j]")
      while j < len(list_copy) and number in list_copy[j]:
        #print(number, "number", "is in listcopy[j]", list_copy[j])
        list_small = []
        for value in list_copy[j]:
          if number == value:
            value = ""
          list_small.append(value)
        #print(list_small)
        list_copy[j].remove(number)
        j = j + 1
        count = (count + 1)
      vertical.append(count)
     
    i = i + 1
  vertical_count = []
  for value in vertical:
    if int(value) == int(size):
      vertical_count.append(value)

  return len(vertical_count)

def diagonal(lista,size):
  diagonal_count = []
  i = 0
  while i < len(lista):
    numlist = lista[i]
    list_copy = copy(lista)
    #print(numlist)
    for value in numlist:
      count = 1 #due to question, has to be one by default
      j = i + 1
      while j < len(list_copy) and (value + 1) in list_copy[j]:
        # if 2, 2+1, 2+2, 2+3 is in list values (list_copy[j])
        for number in list_copy:
          if number == value + 1:
            (value + 1) == ""
        value = value + 1
        count = count + 1
        j = j + 1

      diagonal_count.append(count)
    i = i + 1

  #print(diagonal_count)
  a = []
  for value in diagonal_count:
    if int(value) == int(size):
      a.append(value)
  return(len(a))

def otherdiagonal(lista, size):
  diagonal_count = []
  i = 0
  while i < len(lista):
    numlist = lista[i]
    list_copy = copy(lista)
    #print(numlist)
    for value in numlist:
      count = 1 #due to question, has to be one by default
      j = i + 1
      while j < len(list_copy) and (value - 1) in list_copy[j]:
        # if 2, 2-1, 2-2, 2-3 is in list values (list_copy[j])
        for number in list_copy:
          if number == value - 1:
            (value + 1) == ""
        value = value - 1
        count = count + 1
        j = j + 1

      diagonal_count.append(count)
    i = i + 1

  #print(diagonal_count)
  a = []
  for value in diagonal_count:
    if int(value) == int(size):
      a.append(value)
  return(len(a))

positions_of_x=[]
size_pattern = sys.argv[1] #the number of the size for the pattern
string="" #list of all the values
for line in sys.stdin:
  line = line.strip()
  string = string + line
  #print(line)
  a = []
  i = 0
  while i < len(line):
    if line[i] != "." and line[i] == "x":
      a.append(i) #append positions
    i += 1
  positions_of_x.append(a)
#print(positions_of_x)
##### Done
c = positions_of_x
d = positions_of_x
copy1 = deepcopy(c) #doesnt work, need a deepcopy.
copy2 = deepcopy(d)
number_rows = []
for item in string.split():
  number_rows.append(horizontal(size_pattern,item))
for value in number_rows:
  number_rows = value

number_rows1 = [] # list for everything
for item in string.split():
  number_rows1.append(vertical(positions_of_x,size_pattern))

for item in string.split():
  number_rows1.append(diagonal(copy1,size_pattern))

for item in string.split():
  number_rows1.append(otherdiagonal(copy2,size_pattern))

total = 0
for values in number_rows1:
 total = total + values

print(number_rows + total)



"""
c = positions_of_x
d = positions_of_x
copy = c 
copy1 = d

i = 0
while i < len(a):#looping through lines
  j = 0
  while j < len(a[i]):
    a[i][
    j = j + 1
  i = i + 1
#print(counter)


print((a[i][j + y - 1]) * number_for_connect)
    if ((a[i][j + y - 1]) * number_for_connect) == "x" * number_for_connect:
"""
