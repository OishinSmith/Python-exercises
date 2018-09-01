import q3_52
import sys

def build_dictionary(filename):
  d = {}
  try:
     with open(filename, "r") as f:
        for line in f.readlines():
           line = line.split()
           d[line[0]] = int(line[1])
     return d
  except FileNotFoundError:
     return

def extract_range(d, low, high):
   try:
       new_d = {}
       for key in d:
          if (low <= d[key] and d[key] <= high):
             new_d[key] = d[key]
       return new_d
   except TypeError:
      return
def main():
    d = q3_52.build_dictionary('mappings_52.txt')
    nd = q3_52.extract_range(d, 5, 15)
    if nd == {}:
       for (k, v) in sorted(nd.items()):
           print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()

