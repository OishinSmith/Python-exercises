
import collections
Student = collections.namedtuple("Student", ["firstname", "surname", "id"])

def show_student(s):
  f = "First name"
  sir = "Surname"
  i = "ID"
  max_length = len(f)
  print("{:>{:d}s}: {:>s}".format(f, max_length, s.firstname))
  print("{:>{:d}s}: {:>s}".format(sir, max_length, s.surname))
  print("{:>{:d}s}: {:>d}".format(i, max_length, s.id))

def main():
  student1 = Student('Joe', 'Mannion', 98365338)
  student2 = Student('Louise', 'Callaghan', 99324761)
  student3 = Student(firstname='Noel', id=99071239, surname='Rooney')
  stulist = [student1, student2, student3]

  for details in stulist:
    show_student(details)

if __name__ == "__main__":
  main()


"""
def show_student(firstname, surname, stud_id):
  f = "First name"
  s = "Surname"
  i = "ID"
  max_length = len(f)
  print("{:>{:d}s}: {:>s}".format(f, max_length, firstname))
  print("{:>{:d}s}: {:>s}".format(s, max_length, surname))
  return("{:>{:d}s}: {:>s}".format(i, max_length, stud_id))
"""


  
