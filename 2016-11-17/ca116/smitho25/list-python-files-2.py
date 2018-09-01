import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
    if files[i].split(".")[-1] == "py":  #im splitting on "." (which is the dot), and then looking for "py"
        with open(files[i], "r") as f:
            line = f.read()
            if len(line) != 0:
                print files[i]
    i = i + 1
