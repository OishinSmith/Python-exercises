#!/usr/bin/env python

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
   if files[i].split(".")[-1] == "py":  #im splitting on "." (which is the dot), and then looking for "py"
      print files[i]
   i = i + 1
