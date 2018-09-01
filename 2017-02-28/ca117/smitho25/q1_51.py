import sys
line = sys.argv[1]
line = list(line)
i = 0
while i < len(line)-1:
   line[i],line[i+1] = line[i+1],line[i]
   i +=2
print("".join(line))
