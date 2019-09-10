#!/usr/bin/env python
import random
print """
  __________
< 0123456789 >
  ----------
         ^__^ 
         (oo)_______
         (__)       )/
            ||----w |
            ||     ||
"""

n={'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}

tp=0
np=0
while True:
  b=random.choice(n.keys())
  print b
  x=raw_input()
  if x.isdigit() and x==str(n[b]):
    tp=tp+1
    print "GOOD JOB!"
    print
  else:
    np=np+1
    print "Correct answer is",n[b]
    print "Try again!"
    print
  print "Score: ",tp,"/",tp+np
