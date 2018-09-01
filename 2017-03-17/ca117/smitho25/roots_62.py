import sys
from math import sqrt
line = sys.stdin.readlines()

def quadratic(a, b, c):
  try:
    if (b ** 2 - (4*(a)*(c))) == 0:
      pos_root1 = (-(b) + sqrt((b ** 2) +(-1 * 4 * a * c))) / (2 * a) #1
      pos_root2 = (-(b) + sqrt((b ** 2) +(-1 * 4 * a * c))) / (2 * a) #2
      return "r1 = {}, r2 = {}".format(pos_root1, pos_root2)
    elif (b ** 2 - (4*(a)*(c))) < 0:
      return(None)
    else:
      pos_root = (-(b) + sqrt((b ** 2) +(-1 * 4 * a * c))) / (2 * a) #3
      neg_root = (-(b) - sqrt((b ** 2) +(-1 * 4 * a * c))) / (2 * a) #4
      return "r1 = {}, r2 = {}".format(pos_root, neg_root)
  except ZeroDivisionError:
    return(None)
  #try:
    #pos_root = ((-1 * b) + sqrt(b ** 2 + -1 * 4 * a * c)) / (2 * (a))
    #neg_root = ((-1 * b) - sqrt(b ** 2 + -1 * 4 * a * c)) / (2 * (a))
    #return("r1 = {:>.1f}, r2 = {:>.1f}".format(pos_root, neg_root))
  #except ValueError:
    #return("None")
  #except ZeroDivisionError:
    #return("None")

def main():
  for numbers in line:
    numbers = numbers.strip().split()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    o_ye = quadratic(a, b, c)
    print(o_ye)

if __name__ == "__main__":
  main()

"""
(b ** 2 - (4*(a)*(c))) == 0:
(b ** 2 - (4*(a)*(c))) < 0:
"""
