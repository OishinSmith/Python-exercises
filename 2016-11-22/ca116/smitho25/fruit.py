fruit = {
   "apple": True,
   "pair": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

import sys
lines = sys.stdin.read().split() 
for words in lines:
   if words in fruit:
     print words
