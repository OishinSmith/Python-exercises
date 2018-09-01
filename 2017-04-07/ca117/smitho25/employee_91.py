class Employee(object):

  def __init__(self, name, num):
    self.name = str(name)
    self.num = int(num)
    self.money = 0

  def wages(self):
    return(0)
 
  def __str__(self):
    print("Name: {}".format(self.name))
    print("Number: {}".format(self.num))
    return("Wages: {:.2f}".format(self.money))

class Manager(Employee):

  def __init__(self, name, num, salary):
    super().__init__(name, num)
    self.money = salary / 52
      
class AssemblyWorker(Employee):

  def __init__(self,name,num,hour_rate=0,hours=0):
    super().__init__(name,num)
    self.money = hour_rate * hours

def main():

  e1 = Manager('Mary', 1, 50000)
  e2 = AssemblyWorker('Fred', 2, 15.50, 40)
  e3 = Employee('Sean', 3)

  print(e1)
  print(e2)
  print(e3)

if __name__ == '__main__':
    main()

