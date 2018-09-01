import sys
line = sys.stdin

def seconds(t):
  [mins, secs] = t.split(":")
  total_time = int(mins) * 60 + int(secs)
  return(total_time)  

def second_to_time(t):
  time_div = t[1] / 60 
  [minute, seconds] = str(time_div).split(".")
  seconds = int((int(seconds) / 100) * 60)
  sequence = (str(minute), str(seconds))
  shiet = ":".join(sequence)
  return(shiet)

d = {}
for sentence in line:
  sentence = sentence.strip().split()
  new_min = seconds(sentence[1])
  for time in sentence[1:]:
    minimum = seconds(time)
    if minimum <= new_min:
      new_min = minimum
  d[sentence[0]] = new_min

minimum_time_name = sorted(d.items(), key = lambda d:d[1])[0]
print("{} : {}".format(minimum_time_name[0], second_to_time(minimum_time_name)))
