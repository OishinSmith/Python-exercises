import sys
import os
files = os.listdir(".")
shebang = "#!/usr/bin/env python"

i = 0 
while i < len(files):
  with open(files[i], "r") as f:
    contents = f.readline()
    lenght = len(contents)
    if files[i].split(".")[-1] == "py" and lenght != 0 or contents[:-1] == shebang:
      print files[i]
  i = i + 1
