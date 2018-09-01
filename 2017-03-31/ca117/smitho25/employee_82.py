class Employee(object):
   next_employee_number = 0

   def __init__(self,name, employee_number = next_employee_number, hourly_rate = 9.25, hours_worked = 0):
      self.name = name
      self.employee_number = Employee.next_employee_number
      self.hourly_rate = hourly_rate
      self.hours_worked = hours_worked
      Employee.next_employee_number = Employee.next_employee_number + 1

   def add_hours(self, other):
      self.hours_worked = self.hours_worked + other
      return(self) # returns the object again


   def wages(self):
      return(self.hours_worked * self.hourly_rate)
      

   def __str__(self):
      print("Name: {}".format(self.name))
      print("ID: {:}".format(self.employee_number))
      print("Hours: {:.2f}".format(self.hours_worked))
      print("Rate: {:.2f}".format(self.hourly_rate))
      return("Wages: {:.2f}".format(self.wages()))
def main():

   # Check class attributes
   print('Checking class attributes...')
   print(Employee.next_employee_number)
    
   # Create two employees
   e1 = Employee('Jimmy')
   e2 = Employee('Mary', hours_worked=12, hourly_rate=12.40)

   # Check string representation
   print('Printing employees...')
   print(e1)
   print(e2)

   # Check adding hours
   print('Checking adding hours...')
   e1.add_hours(10.5)
   e2.add_hours(30)
   print(e1)
   print(e2)

   # Check class attributes
   print('Checking class attributes...')    
   print(Employee.next_employee_number)

if __name__ == '__main__':
   main()
