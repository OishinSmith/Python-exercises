class  Weight(object):
  OUNCES_PER_POUND = 16
  def __init__(self, pounds = 0, ounces = 0):
    self.pounds = pounds
    if ounces > Weight.OUNCES_PER_POUND:
      self.ounces = ounces % OUNCES_PER_POUND
    else: 
      self.ounces = ounces

  def __eq__(self, other):
    return self.total() == other.total()

  def __gt__(self, other):
    return(self.total() > other.total())

  def __ge__(self, other):
    return(self.total() >= other.total())

  def __add__(self, other): #add and iadd correlate to eachother
    return Weight.from_ounces(self.total() + other.total())

  def __iadd__(self, other):
    z = self + other
    self.pounds, self.ounces = z.pounds, z.ounces
    return(self)

  def __mul__(self, other):
    return Weight.from_ounces(self.total() * other)
    
  def __imul__(self, other):
    z = self * other
    self.pounds, self.ounces = z.pounds, z.ounces
    return(self)
  def total(self):
    return self.pounds * Weight.OUNCES_PER_POUND + self.ounces

  @classmethod
  def from_ounces(cls, other):
    pounds = int(other / Weight.OUNCES_PER_POUND)
    ounces = (other % Weight.OUNCES_PER_POUND)
    return(cls(pounds, ounces))

  def __str__(self):
    return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)


def main():

    # Create some weights
    w1 = Weight(1, 10)
    w2 = Weight(3, 12)
    w3 = Weight(8, 6)

    # Addition
    print('Addition...')
    w4 = w1 + w2
    print(w4)
    print(w4 > w1)

    # In-place addition
    print('In-place addition...')
    w1_alias = w1
    w1 += w2
    print(w1)
    print(w1 > w1)
    print(w1_alias == w1)

    # Multiplication
    print('Multiplication...')
    w5 = w2 * 2
    print(w5)

    # In-place multiplication
    print('In-place multiplication...')
    w3_alias = w3
    w3 *= 2
    print(w3)
    print(w3 > w1)
    print(w3_alias == w3)

if __name__ == '__main__':
    main()

