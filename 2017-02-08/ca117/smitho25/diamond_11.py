import sys
middle_number = int(sys.argv[1])


for position in range(middle_number * 2):
  if position < middle_number:
    print(" " * (middle_number - int(position) - 1) + ("* " * int(position)) + "*")
  elif position > middle_number:
    print(" " * (position - middle_number) + "* " * (((middle_number * 2) - position) - 1) + "*")

"""
line_k = ""
i = 0
while i < int(middle_number * 2):
  if i < middle_number:
    line_k =(middle_number - i - 1) * " " + ("* " * (i + 1)) 
    print(line_k)

  elif i > middle_number:
    line_k =(" " * (i - middle_number) + "* " * (((middle_number * 2) - i) - 1) + "*")
    print(line_k)
  i = i + 1


while i < int(middle_number):
  asterisk = asterisk + "*"
  i = i + 1
  print(asterisk)



for c in range(middle_number - 1):
    print((middle_number - c - 1) * " " + ("* " * (c + 1)), end="")
for c in range(middle_number - 1, -1, -1):
    print((middle_number - c - 1) * " " + ("* " * (c + 1)), end="")

lines_in_diamond = (2 *(middle_number) - 1)



k = 0
i = 0
while i < (lines_in_diamond):
  number_of_leading_spaces = (middle_number - middle_number - 1) * " "
  number_of_asterisks = "* " * (line_k[i] + 1)

"""
