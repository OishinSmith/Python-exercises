import sys
points = int(sys.argv[1])
goals = 0
while goals * 3 <= points:
   print goals,points - (3 * goals)  
   goals = goals + 1

