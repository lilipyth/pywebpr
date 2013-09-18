#!/usr/bin/env python

# the default value of a function-argument is evaluated only once.
# this causes important differences when using mutable objects as default values.

def f(a, L=[]):      # L=[] is the default argument.
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

# this will print 

# [1]
# [1, 2]
# [1, 2, 3]

# how to prevent default values of function-arguments to be shared between subsequent function-calls.

def e(a, L=None):
    if L is None: 
       L = []
    L.append(a)
    return L

# this will print

print e(1)
print e(2)
print e(3)

# [1]
# [2]
# [3]
