import sys
dst = sys.argv[1]

with open(dst, "w") as f_dst:
  f_dst.write("hello world. \n")

