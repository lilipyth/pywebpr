#!/usr/bin/env python

# rather than always iterating over an arithmetic progression of numbers (like pascal),
# or giving the user the ability to define both the iteration step and halting condition (as c), 
# python's for statement iterates over the itams of any sequence (a list or a string)
# in the order that they appear in the sequence 

a = ['cat', 'window', 'defenestrasse']
print(a)
for x in a:
    print x, len(x)

# modification of the sequence during iteration can only happen for mutable sequence types such as lists.
b = ['door', 'desk','beerbrewery']
print(b)
# b[:] ... creates shallow copy of list b. 
# needed if modifications should be applied to elements in list during iteration.
for x in b[:]:
    if len(x) > 6:  b.insert(0, x)

print(b)
