import sys
line = sys.stdin

month = {
"January" : "1",
"February" : "2",
"March" : "3",
"April" : "4",
"May" : "5",
"June" : "6",
"July" : "7",
"August" : "8",
"September" : "9",
"October" : "10",
"November" : "11",
"December" : "12",
}

for date in line:
  [d, m, y] = date.strip().split()
  print(d + "/" + month[m] + "/" + y[-2:])
