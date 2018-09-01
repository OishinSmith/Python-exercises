import sys
filename = sys.argv[1] #file name is just labeling the invocation for the "real" file name

with open(filename, "w") as f: #so if filename is "somefile.txt", the with command will open it and will write ("w") stuff in it.
  i = 2 
  while i < len(sys.argv):
     f.write(sys.argv[i] + "\n") #loops command lines/invocations as many times as i < len(sys.argv)
     i += 1
