import sys
import math
from math import pi

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))
    #for r in range(int(start_r), int(end_r), int(inc_r)):
      #print('{:>10.1f} {:>10.2f} {:>10.2f}'.format(r, 4 * pi * r ** 2, (4 / 3) * pi * r ** 3))
    
  
    while start_r <= (end_r):
      print('{:>10.1f} {:>15.2f} {:>15.2f}'.format(start_r, 4 * pi * start_r ** 2, (4 / 3) * pi * start_r ** 3))
      start_r = start_r + inc_r      
      
if __name__ == '__main__':
    main()


  
 

