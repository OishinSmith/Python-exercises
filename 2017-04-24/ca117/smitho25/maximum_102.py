def maximum(list_1):
  i = 0

  total = 0
  while i < len(list_1):
    if int(list_1[i]) >= int(total):
      total = list_1[i]
    else:
      pass
    i = i + 1
  return(total)

def main():
    max = None
    print(maximum([6,5,1,3,4]))
    print(maximum([6,5,11,3,4]))
    print(maximum([6,15,11,13,14]))
    print(maximum([6,15,11,13,4]))

if __name__ == '__main__':
    main()

