class Weight(object):
  OUNCES_PER_POUND = 16
  new_ounces = 17
    
  def __init__(self, pounds = 0, ounces = 0):
    self.pounds = pounds
    self.ounces = ounces 
    self.OUNCES_PER_POUND = 16
 
  def to_ounces(self):
    return self.pounds * self.OUNCES_PER_POUND + self.ounces
 
  def __eq__(self,other):
    return self.to_ounces() == other.to_ounces()
 
  def __gt__(self, other):
    return(self.to_ounces() > other.to_ounces())
 
  def __ge__(self, other):
    return(self.to_ounces() >= other.to_ounces())

  def __add__(self, other):
    return Weight.from_ounces(self.to_ounces() + other.to_ounces()) 

  def add_ounces(self, other):
    pass

  def __iadd__(self, other):
    (self.pounds) += other.pounds
    (self.ounces) += other.ounces
    if self.ounces >= 16:
      self.pounds, self.ounces = self.pounds + 1, int(self.pounds % 16) + 2
    return self
    #return(Weight.from_ounces(self.to_ounces()))

  def __mul__(self,other):
    return(Weight.from_ounces(self.to_ounces() * other))

  def __imul__(self, other):
    self.pounds *= other
    self.ounces *= other
    return(self)

  #def __lt__(self, other)
  @classmethod
  def from_ounces(cls, total_ounces):
    pounds, ounces = divmod(total_ounces, cls.OUNCES_PER_POUND)
    return(cls(pounds, ounces))
  
  def __str__(self):
    return("{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces))
      
  


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
    w1_alias = w1 #(1,10)
    w1 += w2
    print("-----------------------")
    print(w1)
    print(w1 > w1)
    print(w1_alias)
    #print(w1_alias == w1)
    print("-----------------------")

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


