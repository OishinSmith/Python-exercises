class Weight(object):
   OUNCES_PER_POUND = 16
   new_ounces = 17
   
   def __init__(self, pounds = 0, ounces = 0):
     self.pounds = pounds
     self.ounces = ounces 

   def __str__(self):
     return("{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces))
 
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
