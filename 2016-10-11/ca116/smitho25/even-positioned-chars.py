s = raw_input()
t = ""
i = 0
while i < len(s):
   if i % 2 == 0:
      t = t + s[i]
   # print i,t
   i = i + 1

print t
