#!/usr/bin/env python

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1 
    while a < n: 
        result.append(a)
        a, b = b, a+b
    return result
    # can't just fall off the end of the fuction. so 'none' will not be returned.

f100 = fib2(100)    # call the fuction
print(f100)         # print result
