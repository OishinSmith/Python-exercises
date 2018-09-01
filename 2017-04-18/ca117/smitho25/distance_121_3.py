class Distance(object):
  YARDS_PER_MILE = 1760
  def __init__(self, miles = 0, yards = 0):
    self.miles = miles
    self.yards = yards

  @classmethod
  def from_yards(cls, other):
    miles = int(other / Distance.YARDS_PER_MILE)
    yards = other % Distance.YARDS_PER_MILE
    return(cls(miles, yards))

  def total(self):
    return self.miles * Distance.YARDS_PER_MILE + self.yards

  def __str__(self):
    return("{} mile(s) and {} yard(s)".format(self.miles, self.yards))

  def __eq__(self, other):
    if self.total() == other.total():
      return("True")
    else:
      return False

  def __gt__(self, other):
    if self.total() > other.total():
      return(True)
    else: 
      return False

  def __ge__(self, other):
    if self.total() >= other.total():
      return(True)
    else: 
      return False

  def __sub__(self, other):
    return Distance.from_yards(self.total() - other.total())

  def __isub__(self, other):
    z = self - other
    self.miles, self.yards = z.miles, z.yards
    return(self)

  def __mul__(self, other):
    return(Distance.from_yards(self.total() * other))

  def __imul__(self, other):
    z = self * other
    self.miles, self.yards = z.miles, z.yards
    return(self)
    
def main():

    # Create some distance objects
    d1 = Distance()
    d2 = Distance(3, 1200)
    d3 = Distance(2, 1400)

    # Subtraction (overriding __sub__)
    print('Subtraction...')
    d4 = d2 - d3
    print(d4)
    print(d4 < d2)

    # In-place subtraction (overriding __isub__)
    print('In-place subtraction...')
    d2_alias = d2
    d2 -= d3
    print(d2)
    print(d2 < d3)
    print(d2_alias is d2)

    # Multiplication
    print('Multiplication...')
    d5 = d3 * 3
    print(d5)

    # In-place multiplication
    print('In-place multiplication...')
    d3_alias = d3
    d3 *= 3
    print(d3)
    print(d3 > d1)
    print(d3_alias is d3)

if __name__ == '__main__':
    main()

