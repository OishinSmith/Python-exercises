import sys

def l2d(f):
  d = {}
  key = f.readline().strip().split()
  value = f.readline().strip().split()
  n = len(key)
  i = 0
  while i < n:
    d[key[i]] = value[i]
    i = i + 1
  return d

def main():
  d = l2d(sys.stdin)
  for (k, v) in sorted(d.items()):
    print("{} : {}".format(k,v))

if __name__ == '__main__':
  main()
