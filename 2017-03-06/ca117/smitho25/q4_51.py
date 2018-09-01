import sys
line = sys.stdin.readlines()

total = 0
for letter in line:
  number = letter.strip()
  number = int(number)
  total = total + (number)
  
avg = total / len(line)
print("Mean: {:>.1f}".format(avg))

d = {}
def sorter(t):
  return(t[-1])
for number in line:
  number = number.strip()
  if number not in d:
    d[number] = 1
  else:
    d[number] = d[number] + 1
  mode_tuple = max(d.items(), key = sorter)  
  mode = mode_tuple[0]

print("Mode: {:>.1f}".format(int(mode)))

N = int(len(line))
snums = sorted(line)
a = []
#print(float((snums[N // 2 - 1] + snums[N // 2])) / float((2.0)))
for number in line:
  number = number.strip()
  a.append(int(number))


a = sorted(a)
if len(a) % 2 == 0:
  sumed = float((a[N // 2 - 1] + a[N // 2]))
  median = sumed / (2.0)
else:
  median = a[N // 2]
  
print("Median: {:>.1f}".format(float(median)))
