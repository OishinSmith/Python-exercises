lines = []
new_line = []
line = raw_input()
while line != "end":
  lines.append(line) 
  line = raw_input() 

rev_lin = "" 
for c in lines: #big ass problem here, brain not working, 3 am. sleep.
  for word in c:
    rev_lin = word + rev_lin 
    new_line.append(rev_lin)

print new_line

"""
    while i < len(lines):
      lines.append(rev_lin)
      i = i + 1
    print lines
"""

"""lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()       

i = 0
while i < len(lines) / 2:
   tmp = lines[i]
   lines[i] = lines[len(lines) - i - 1]
   lines[len(lines) - i - 1] = tmp
   i = i + 1

i = 0
while i < len(lines):
  print lines[i]
  i = i + 1

"""
