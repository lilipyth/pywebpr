#!/usr/bin/env python

# finds prime numbers in the interval [2, 9]

for n in range(2, 10): 
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    # the else clause belongs to the for loop, not to the if statement
    # the else clause is terminated through the exhaustion of the range the for-loop iterates over.
    else:
        # loop fell through without finding a factor 
        print n, 'is a prime number'
