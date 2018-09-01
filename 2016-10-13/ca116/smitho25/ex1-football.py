homegoals = input()
homepoints = input()
awaygoals = input()
awaypoints = input()


hometotal = (homegoals * 3) + homepoints
awaytotal = (awaygoals * 3) + awaypoints
if hometotal == awaytotal:
  print "draw"
elif hometotal < awaytotal:
  print "away win"  
else:
  print "home win"


