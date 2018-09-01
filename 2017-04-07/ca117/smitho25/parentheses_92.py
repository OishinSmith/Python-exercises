from stack_92 import Stack
def matcher(line):
  s = Stack()
  p = ["()", "[]", "{}"]
  bracks = "([}"
  try:
    for bracket in line:
      if bracket in "([{":
         s.push(bracket)
      if bracket in ")]}":
         if s.is_empty():
            return False
         stack_pop = s.pop()
         if stack_pop + bracket not in p:
            return False
    return s.is_empty()
  except IndexError:
    pass

import sys
def main():
  
  for line in sys.stdin:
    print(matcher(line.strip()))

if __name__ == '__main__':
  main()

