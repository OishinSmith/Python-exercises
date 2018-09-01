import sys
import string
lines = sys.stdin.readlines()
par = lines[0].strip().split()
index = lines[1].strip().split()
i = 0
def free_strokes(handicap, index):
  handicap = int(handicap)
  index = int(index)
  free_strok = 0
  total = 0
  if handicap < 18:
    if index in range(1, (handicap) + 1): #+1 since i starts at 0
      return(1)
    else:
      return(0)
  else:
    free_strok = int(handicap / 18)
    total = handicap - (free_strok * 18)
    if index in range(1, (total + 1)):# +1 since i = 0
      return 1 + free_strok # +1 due to an error
    else:
      return free_strok
    
def main():
  d = {
  "-7" : 9,
  "-6" : 8,
  "-5" : 7,
  "-4" : 6,
  "-3" : 5,
  "-2" : 4,
  "-1" : 3,
  "0" : 2,
  "1" : 1,
  "2" : 0,

  }

  e = {}
  f = []
  disqualified = {}
  points = 0
  grand_total = 0
  for word in lines[2:]:
    word = word.strip().split()
    name = " ".join(word[:-19])
    handicap = word[-19] 
    stroke = word[-18:]
    i = 0
    points =  0
  
    while i < 18:

      pa,ind,st = par[i], index[i], stroke[i]
      i = i + 1
      grand_total = 0
      if st.isdigit():
        freestroke = free_strokes(handicap, ind)
        net_stroke = int(st) - freestroke
        net_strok = net_stroke - int(pa)
        if str(net_strok) in d:
          grand_total = d[str(net_strok)]
        else:
          grand_total = 0 
      elif st == "X":
          pass
               
      else:
        st = "Disqualified"
        f.append(name)
        break
      points = points + grand_total
      e[name] = points


  def sorter(t):
    return t[1]
  d = {} 

  e_copy = {} #need a copy because the e.copy() below will be changed
  for k,v in e.copy().items():
    e_copy[k] = v

  for k, v in e.copy().items():
    if k in f:
      disqualified[k] = "Disqualified"
      del e[k]

  max_len = 0
  for length in e_copy.keys():
    if len(length) > max_len:
      max_len = len(length)
 
  max_len2 = 0
  for length in e_copy.values():
    if len(str(length)) > max_len2:
      max_len2 = len(str(length))

  for k, v in sorted(e.copy().items(), key = sorter, reverse = True):
    print("{:>{}} : {:>{}}".format(k, max_len, v, max_len2))


  for value in f:
    print("{:>{}} : {:>{}}".format(value, max_len, "Disqualified", max_len2))

if __name__ == "__main__":
  main()
"""
for k, v in sorted(disqualified_1.items(), key = sorter, reverse = False):
  print("{:>{}} : {:>{}}".format(k, max_len, disqualified[k], max_len2))
"""

"""
print(e)
def sorter(t):
  return t[1]
  d = {} 

for k, v in e.copy().items():
  if k in f:
    disqualified[k] = "Disqualified"
    del e[k]

max_len = 0
for length in e.keys():
  if len(length) > max_len:
    max_len = len(length)
 
max_len2 = 0
for length in e.values():
  if len(str(length)) > max_len2:
    max_len2 = len(str(length))

for k, v in sorted(e.items(), key = sorter, reverse = True):
  print("{:>{}} : {:>{}}".format(k, max_len, v, max_len2))

for k, v in disqualified.items():
  print("{:>{}} : {:>{}}".format(k, max_len, v, max_len2))
"""




"""
import sys
import string
lines = sys.stdin.readlines()
par = lines[0].strip().split()
index = lines[1].strip().split()
i = 0
d = {
  "-7" : 9,
  "-6" : 8,
  "-5" : 7,
  "-4" : 6,
  "-3" : 5,
  "-2" : 4,
  "-1" : 3,
  "0" : 2,
  "1" : 1,
  "2" : 0,
  "3" : 0,
  "4" : 0,
  "5" : 0,
  "6" : 0,
  "7" : 0,
  "8" : 0,
  "9" : 0, 
}

e = {}
f = []
disqualified = {}
points = 0
for word in lines[2:]:
  word = word.strip().split()
  name = " ".join(word[:-19])
  handicap = word[-19] 
  stroke = word[-18:]
  i = 0
  points =  0
  while i < len(par):
    pa,ind,st = par[i], index[i], stroke[i]
    i = i + 1
    if st.isdigit() or st == "X":
      if st == "X":
        continue
      #if st != "abcdefghijklmnopqrstuvwyz":
        
      if int(handicap) == 0:
        total = int(st) - 0
        total = total - int(pa)
        if str(total) in d:
          grand_total = d[str(total)]

      elif 1 <= int(handicap) <= 18:
     
        if int(ind) <= int(handicap):
          net_stroke = int(st) - 1
          net_stroke = net_stroke - int(pa)
          if str(net_stroke) in d:
            grand_total = d[str(net_stroke)]

        elif int(ind) > int(handicap):
          total = int(st) - 0
          total = total - int(pa)
          if str(total) in d:
            grand_total = d[str(total)]

      elif 18 < int(handicap) <= 36:
        if int(ind) <= int(handicap):
          net_stroke = int(st) - 2
          net_stroke = net_stroke - int(pa)
          if str(net_stroke) in d:
            grand_total = d[str(net_stroke)]

        elif int(ind) > int(handicap):
          total = int(st) - 1
          total = total - int(pa)
          if str(total) in d:
            grand_total = d[str(total)]

      elif 36 < int(handicap) <= 54:
        if int(ind) <= int(handicap):
          net_stroke = int(st) - 3
          net_stroke = net_stroke - int(pa)
          if str(net_stroke) in d:
            grand_total = d[str(net_stroke)]

        elif int(ind) > int(handicap):
          total = int(st) - 2
          total = total - int(pa)
          if str(total) in d:
            grand_total = d[str(total)]
      
      f.append(name)
    
    points = points + grand_total
  e[name] = points

print(e)
def sorter(t):
  return t[1]
  d = {} 

for k, v in e.copy().items():
  if k in f:
    disqualified[k] = "Disqualified"
    del e[k]

max_len = 0
for length in e.keys():
  if len(length) > max_len:
    max_len = len(length)
 
max_len2 = 0
for length in e.values():
  if len(str(length)) > max_len2:
    max_len2 = len(str(length))

for k, v in sorted(e.items(), key = sorter, reverse = True):
  print("{:>{}} : {:>{}}".format(k, max_len, v, max_len2))

for k, v in disqualified.items():
  print("{:>{}} : {:>{}}".format(k, max_len, v, max_len2))
"""

