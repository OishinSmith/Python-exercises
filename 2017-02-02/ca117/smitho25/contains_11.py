import sys

def cont(letter, string):
  for c in letter:
    if c in string:
      string = string.replace(c, "", 1)
    else:
      return False
  return True

print(cont(sys.argv[1], sys.argv[2]))
