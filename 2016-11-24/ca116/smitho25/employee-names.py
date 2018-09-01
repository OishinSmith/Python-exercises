import sys 
with open("employees.txt") as lines:
  lines = lines.read().split("\n")
e = {}
i = 0
while i < len(lines):
  if lines[i] != "":
    id_date_of_birth_employee_name = lines[i].split()
    e_id = id_date_of_birth_employee_name[0]
    d_o_b = id_date_of_birth_employee_name[1]
    e_name = " ".join(id_date_of_birth_employee_name[2:])
    d = {
        "id": e_id,
        "name": e_name,
        "dob": d_o_b,
    }
    e[e_id] = d
  i += 1

employees_numbers = sys.stdin.read().split()
for number in employees_numbers:
  if number in e:
    print e[number]["name"] 
