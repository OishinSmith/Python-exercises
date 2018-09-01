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
def main():

    # Create some distance objects
    d1 = Distance()
    d2 = Distance(3, 1200)
    d3 = Distance(3, 1200)

    # Confirm all objects are instances of Distance
    assert(isinstance(d1, Distance))
    assert(isinstance(d2, Distance))
    assert(isinstance(d3, Distance))
    
    # Equality
    print('Equality...')
    print(d2 == d3)
    print(d1 == d2)
    print(d2 != d3)

    # Greater than, greater than or equal to
    print('Greater than, greater than or equal to...')
    print(d1 > d2)
    print(d2 > d1)
    print(d2 >= d3)

    # Less than, less than or equal to
    print('Less than, less than or equal to...')
    print(d1 < d2)
    print(d2 < d1)
    print(d2 <= d3)

if __name__ == '__main__':
    main()

