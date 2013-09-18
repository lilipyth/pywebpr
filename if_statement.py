#!/usr/bin/env python

# ask the user for an integer of his or her choice.
x = int(raw_input("Please enter an integer: "))

if x < 0:
    x = 0 
    print 'Negative changed to zero'
elif x == 0: 
    print 'Zero'
elif x == 1:
    print 'Single'
elif x == 2:
    print 'Dual'
elif x == 3: 
    print 'Triple'
elif x == 4: 
    print 'Quad'
else: 
    print 'More'
