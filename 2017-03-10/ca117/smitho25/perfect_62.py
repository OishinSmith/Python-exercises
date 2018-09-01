import sys
lines = sys.stdin.readlines()
  
def sumFac(n):
  list_n = range((n//2)+1)
  total = 0
  for number in list_n:
    if number != 0 and n % number == 0 and number != n:
      total = total + number
  return(total)

def isPerfect(n):
  if sumFac(n) == n:
    return(True)
  else:
    return(False)
def main():
  for number in lines:
    print(isPerfect(int(number)))

if __name__ == "__main__":
  main()

