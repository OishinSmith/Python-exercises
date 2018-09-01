#in computing, a shebang is the character sequence consisting of the characters number sign and exclamation mark (#!) at the beginning of a script. It is also called sha-bang,[1][2] hashbang,[3][4] pound-bang,[5] or hash-pling.
import sys
import os
files = os.listdir(".")
shebang = "#!/usr/bin/env python"

i = 0 
while i < len(files):
  with open(files[i], "r") as f:
    first-line = f.readline()
    content = len(files)
    if files[-3] == ".py" and first-line[:1] == shebang or content != 0:
      print files[i]
  i = i + 1
 
