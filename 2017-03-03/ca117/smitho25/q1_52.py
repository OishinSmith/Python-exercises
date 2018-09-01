import sys
string = sys.argv[1]
number = int(sys.argv[2])
number = number % len(string)
end = (string[len(string) - (number):])
  
print(end + string[:len(string) - (number)])
