#!/usr/bin/env python

i =5 
def f(arg=i):
    print arg

i = 6 
# will return 5
f()
