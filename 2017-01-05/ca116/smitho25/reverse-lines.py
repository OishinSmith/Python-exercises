lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

n = len(lines)         
i = 0                  
while i < n:
   print lines.pop()
   i = i + 1#this doesnt really work, so we have to use the code in the bottom part in pink

"""i = 0
while i < len(lines)/2:
   tmp = lines[i]
   lines[i] = lines[len(lines) - i - 1]
   lines[len(lines) - i - 1] = tmp
   i = i + 1

i = 0
while i < len(lines):
  print lines[i]
  i = i + 1
"""
