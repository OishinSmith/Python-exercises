import sys

food_calorie = {}
with open(sys.argv[1], "r") as f:
  for sentence in f:
    sentence = sentence.strip().split()
    joined_name_for_food = (" ".join(sentence[0:-1]))
    food_calorie[joined_name_for_food] = sentence[-1]
    
diet = sys.stdin.readlines()
for line in diet:
  line = line.strip().split(",")
  food = line[1:]
  for word in food:
    if word in food_calorie:
      food_calorie[word] 
    else:  
      food_calorie[word] = 100

d = {}
name_list = []
number_list =[]
for line in diet:
  line = line.strip().split(",")
  food = line[1:]
  name = line[0]
  name_list.append(name)
  total_calories = 0
  for word in food:
    if word in food_calorie:
      total_calories = total_calories + int(food_calorie[word])
  d[name] = total_calories
  number_list.append(total_calories)
max_len_v = len(str(max(number_list)))
max_name_length = int(len(max(name_list)))

for k, v in sorted(d.items(), key = lambda d:d[1], reverse = False):
  print("{:>{}} : {:>{}}".format(k, max_name_length, v, max_len_v))

      
