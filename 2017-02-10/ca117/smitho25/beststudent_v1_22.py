import sys

try:
  with open(sys.argv[1], "r") as f:
    highest_mark = 0
    lines = f.readlines()
  
    for sentence in lines:
      sentence = sentence.strip().split(" ")
      if int(sentence[0]) > int(highest_mark):
        highest_mark = sentence[0]
        best_student = " ".join(sentence[1:])
    print("Best student: " + best_student)
    print("Best mark: " + str(highest_mark))
            
except FileNotFoundError:
  print('The file {:s} does not exist.'.format(sys.argv[1]))





