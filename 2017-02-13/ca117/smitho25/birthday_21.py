import sys
import calendar

day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])

day_sentences = {

0 : "Monday's child is fair of face.",
1 : "Tuesday's child is full of grace.",
2 : "Wednesday's child is full of woe.",
3 : "Thursday's child has far to go.",
4 : "Friday's child is loving and giving.",
5 : "Saturday's child works hard for a living.",
6 : "Sunday's child is fair and wise and good in every way.",

}

days_ot_week = {

0 : "Monday",
1 : "Tuesday",
2 : "Wednesday",
3 : "Thursday",
4 : "Friday",
5 : "Saturday",
6 : "Sunday",

}

week_day = calendar.weekday(year, month, day) #returns 0-6 = monday to sunday
#print(week_day)

print("You were born on a {} and {}".format((days_ot_week)[week_day], (day_sentences)[week_day]))

"""
days_ot_week = {

"Monday" : "Monday’s child is fair of face",
"Tuesday" : "Tuesday’s child is full of grace.",
"Wednesday" : "Wednesday’s child is full of woe.",
"Thursday" : "Thursday’s child has far to go.",
"Friday" : "Friday’s child is loving and giving.",
"Saturday" : "Saturday’s child works hard for a living.",
"Sunday" : "Sunday’s child is fair and wise and good in every way.",

}

for day in days_ot_week:
  print(day)
  print(days_ot_week[day])

"""
