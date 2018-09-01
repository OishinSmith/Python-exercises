class Customer(object):
  discount = 0
  def __init__(self,name,balance, addr_line1, addr_line2,addr_line3):
    self.name = name
    self.balance = float(balance)
    self.add1 = str(addr_line1)
    self.add2 = str(addr_line2)
    self.add3 = str(addr_line3)



  def d(self):
    return self.balance * self.discount
  
  def due(self):
    return self.balance - self.d()
  
  def __str__(self):
    print("{}".format(self.name))
    print("{}".format(self.add1))
    print("{}".format(self.add2))
    print("{}".format(self.add3))
    print("Balance: {:.2f}".format(self.balance))
    print("Discount: {:.0f}%".format(self.discount*100))
    return("Amount due: {:.2f}".format(self.due()))

class ValuedCustomer(Customer):
  discount = 0.1
 
def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
    c2 = ValuedCustomer('Lucy', 50, '23 Main Street', 'Roosky', 'Roscommon');
    c3 = Customer('Fred', "100", '24 Main Street', 'Sneem', 'Kerry');

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
  main()


