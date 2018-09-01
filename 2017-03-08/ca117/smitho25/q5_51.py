import sys
line = sys.stdin

def seconds(t):
  try:
    [mins, secs] = t.split(":")
    total_time = int(mins) * 60 + int(secs)
    return(total_time)  
  except ValueError:
    pass

def second_to_time(t):
  time_div = t[1] / 60 
  [minute, seconds] = str(time_div).split(".")
  if len(seconds) == 2:
    seconds = int((int(seconds) / 100) * 60)
    sequence = (str(minute), str(seconds))
    shiet = ":".join(sequence)
  elif len(seconds) == 1:
    seconds = int(seconds) * 10
    seconds = int((int(seconds) / 100) * 60)
    sequence = (str(minute), str(seconds))
    if len(sequence[1]) != 2:
      shiet = ":".join(sequence)[0:3] + "0"
    else:
      shiet = ":".join(sequence)
  return(shiet)

d = {}

for sentence in line:
  try:
    sentence = sentence.strip().split()
    new_min = seconds(sentence[1])
    for time in sentence[1:]:
      minimum = seconds(time)
      if int(minimum) <= int(new_min):
        new_min = minimum
      d[sentence[0]] = new_min
  except TypeError:
    pass

minimum_time_name = sorted(d.items(), key = lambda d:d[1])[0]
print("{} : {}".format(minimum_time_name[0], second_to_time(minimum_time_name)))
