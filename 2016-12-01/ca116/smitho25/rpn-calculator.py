import sys
import math
stack = []

def sums(a, b):
  return a + b

def subtract(a,b):
  return a - b

def divide(a, b):
  return a / b

def multiply(a,b):
  return a * b
 
def power(a,b):
  return a ** b

def square(a):
  return a ** 2

def negate(a):
  return -a

def log(a):
  return math.log(a)

def root(a):
  return a ** 0.5


signs = {
  "+" : sums,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,
  "**" : power,
}

unary = { 
 "s" : square,
 "n" : negate,
 "r" : root,
 "l" : log
}

token = sys.stdin.read().split()
for word in token:
  if word in signs:
    b = stack.pop()
    a = stack.pop()
    math = signs[word]
    c = math(a,b)
    stack.append(c)
  elif word in unary:
    a = stack.pop()
    math = unary[word]
    c = math(a)
    stack.append(c)
  elif word == "p":
    print stack[len(stack) - 1]
  else:
    stack.append(float(word))
