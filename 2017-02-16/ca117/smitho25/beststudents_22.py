import sys
 
 
with open(sys.argv[1], "r") as f:
  highest_mark = 0
  lines = f.readlines()
  
  for sentence in lines:
    try:
      sentence = sentence.strip().split(" ")
      if int(sentence[0]) > int(highest_mark):
        highest_mark = sentence[0]
        best_student = " ".join(sentence[1:])
      elif int(sentence[0]) == int(highest_mark):
        best_student = best_student + ", " + " ".join(sentence[1:])
    except ValueError:
      print("Invalid mark {} encountered. Skipping.".format(sentence[0]))
  print("Best student(s): " + best_student)
  print("Best mark: " + str(highest_mark))
