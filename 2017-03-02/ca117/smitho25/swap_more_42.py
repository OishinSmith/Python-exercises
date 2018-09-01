import sys

def swap_unique_keys_values(d):
  #my_dict = d
  
  #new_dict = {v : k for (k, v) in my_dict.items()}
  #return(new_dict)
  c = {}
  e = []
  r = {}
  seen = {}
  for value in d.values():
    if value not in c:
      c[value] =  1
    else:
      c[value] = c[value] + 1
  
  for (keys, values) in c.items():
    if values == 2:
      e.append(keys)
      del values

  for key in e:
    for value in d.items():
      if key not in value:
        r[value[0]] = value[1]
  my_dict = r
  new_dict = {v : k for (k, v) in my_dict.items()}    
  return(new_dict)


def main():
  new_dict = swap_unique_keys_values(d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7,}) 
  print(new_dict.items())
   
if __name__ == "__main__":
  main()

"""
 

d = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7,}
c = {}
e = []
r = {}
seen = {}
for value in d.values():
  if value not in c:
    c[value] =  1
  else:
    c[value] = c[value] + 1
  
for (keys, values) in c.items():
  if values == 2:
    e.append(keys)
    print(keys)
    del values
print(e)

for key in e:
  print(d.items())
  print(key)
  for value in d.items():
    print(value)
    if key not in value:
      print(True)
      r[value[0]] = value[1]
      
print(r)
    
"""

