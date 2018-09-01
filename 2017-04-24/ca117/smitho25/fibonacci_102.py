def fibonacci(pos):
  import sys
  prev = 0
  curr = 1
  i = 0
  if pos == 0:
    return(1)
  else:
    while i < pos + 1:
      curr = prev + curr
      prev = curr-prev
      i = i + 1
    return(prev)
def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(5))
    print(fibonacci(8))

if __name__ == '__main__':
    main()

