def isfloat(a):
  if a.isdigit():
    return True
  elif "." in a:
    return(a.split(".")[1].isdigit())
  


def r(n): #root
  return(abs(n) ** 0.5)

def negative(n):#sign converter
  return -n

def sub(a, b): #subtract 
  return(b - a)

def a(a, b): # add
  return(a + b)

def m(a, b): #multiply 
  return(a * b)

def d(a, b): # divide
  return(b / a)

def calculator(line):

  integer = {
    "r":r,
    "n":negative
  }
  sign = {
    "+" : a,
    "-" : sub,
    "*" : m,
    "/" : d,
  }
  list_1 = []
  for value in line.split():
    if isfloat(value):
      list_1.append(float(value))
    elif value in integer:
      list_1.append(integer[value](list_1.pop()))
    elif value in sign:
         list_1.append(sign[value](list_1.pop(),list_1.pop()))
  return list_1[-1]


import sys
def main():

  for line in sys.stdin:
    try:
      a = calculator(line.strip())
      print('{:.2f}'.format(a))
    except IndexError:
      print('Invalid RPN expression')

if __name__ == '__main__':
    main()


