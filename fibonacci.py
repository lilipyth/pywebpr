#!/usr/bin/env python
# Fibonacci series:
# The sum of two elements defines the next

a, b = 0, 1 

while b < 10: 
    print b 
    a, b = b, a + b

a, b = 0, 1 

while b < 10:
    # a trailing comma avoids the newline after the output
    print b, 
    a, b = b, a + b
