#!/usr/bin/env python
import random
print """
  __________________________
< ABCDEFGHIJKLMNOPQRSTUVWXYZ >
  --------------------------
           ^__^ 
           (oo)_______
           (__)       )/
              ||----w |
              ||     ||

"""

s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tp=0
np=0
while True:
  b=random.choice(s)
  l=b.lower()
  print l
  x=raw_input()
  if x.upper()==b:
    tp=tp+1
    print "GOOD JOB!"
    print
  else:
    np=np+1
    print "Try again!"
    print
  print "Score: ",tp,"/",tp+np

