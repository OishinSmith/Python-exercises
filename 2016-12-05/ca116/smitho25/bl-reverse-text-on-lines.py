"""
line = raw_input()
while line != "end":
   start = ""
   end = ""
   j = 0
   while j < len(line) / 2:
      end = line[j] + end
      start += line[len(line) - 1 - j]
      j += 1
   print start + end
   line = raw_input()
"""

line = raw_input()
while line != "end":
	rev_lin = "" 
	for letter in line:
		rev_lin = letter + rev_lin 
	print rev_lin
	line = raw_input()
