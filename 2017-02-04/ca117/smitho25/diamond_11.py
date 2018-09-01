import sys
middle_number = int(sys.argv[1])

"""
line_k = ""
i = 0
while i < int(middle_number):
  line_k =(middle_number - i - 1) * " " + (2 * i + 1) * (" " + "*") 
  print(line_k)
  i = i + 1
i = 0
while i < int(middle_number):
  line_k =(middle_number - i - 1) * " " + (2 * i + 1) * (" " + "*") 
  print(line_k)
  i = i + 1


while i < int(middle_number):
  asterisk = asterisk + "*"
  i = i + 1
  print(asterisk)

"""

for c in range(middle_number - 1):
    print((middle_number - c - 1) * " " + ("* " * (c + 1)))
for c in range(middle_number - 1, -1, -1):
    print((middle_number - c - 1) * " " + ("* " * (c + 1)))
    
