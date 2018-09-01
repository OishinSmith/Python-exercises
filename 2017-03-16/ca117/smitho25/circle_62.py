import sys
def overlap(x1 = 0, y1 = 0, r1 = 0, x2 = 0, y2 = 0, r2 = 0):
  if x1 == x2 and y1 == y2 and r1 == r2:
    return True
  distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
  if abs(distance) <= r1:
    return True
  if abs(distance) <= r2: 
    return True
  else:
    return(False)

def main():
  x1 = 0
  y1 = 0
  r1 = 0
  x2 = 0
  y2 = 0
  r2 = 0
  print(overlap())
  
  print(overlap(10))
  print(overlap(10,10))
  print(overlap(10,10,10))
  print(overlap(10,0,10))
  print(overlap(10,0,1,8,0,1))
  print(overlap(10,0,1,8,0,2))

if __name__ == '__main__':
    main()


