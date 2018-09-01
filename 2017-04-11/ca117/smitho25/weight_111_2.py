class Weight(object):
  OUNCES_PER_POUND = 16
  new_ounces = 17
   
  def __init__(self, pounds = 0, ounces = 0):
     self.pounds = pounds
     self.ounces = ounces 

  def __str__(self):
     return("{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces))

  def to_ounces(self):
    return self.pounds * self.OUNCES_PER_POUND + self.ounces

  def __eq__(self,other):
    return self.to_ounces() == other.to_ounces()

  def __gt__(self, other):
    return(self.to_ounces() > other.to_ounces())

  def __ge__(self, other):
    return(self.to_ounces() >= other.to_ounces())

  #def __lt__(self, other)
  @classmethod
  def from_ounces(cls, total_ounces):
     pounds, ounces = divmod(total_ounces, cls.OUNCES_PER_POUND)
     return(cls(pounds, ounces))
     
 
def main():
 
     # Create some weights
     w1 = Weight()
     w2 = Weight(3, 12)
     w3 = Weight.from_ounces(100)
 
     # Check all are instances of Weight
     assert(isinstance(w1, Weight))
     assert(isinstance(w2, Weight))
     assert(isinstance(w3, Weight))
     
      #Display ounces per pound
     print('Ounces in a pound: {}'.format(Weight.OUNCES_PER_POUND))
 
     # Display weights
     print('Weights...')
     print(w1)
     print(w2)
     print(w3)
 
if __name__ == '__main__':
     main()

def main():

    # Create some weights
    w1 = Weight(1, 10)
    w2 = Weight(3, 12)
    w3 = Weight(3, 12)

    # Equality
    print('Equality...')
    print(w2 == w3)
    print(w1 == w2)
    print(w2 != w3)

    # Greater than, greater than or equal to
    print('Greater than, greater than or equal to...')
    print(w1 > w2)
    print(w2 > w1)
    print(w2 >= w3)

    # Less than, less than or equal to
    print('Less than, less than or equal to...')
    print(w1 < w2)
    print(w2 < w1)
    print(w2 <= w3)

if __name__ == '__main__':
    main()

