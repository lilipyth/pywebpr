#!/usr/bin/env python

# if you need to iterate over a sequence of numbers, use range()
# use like seen below

# calculate ranges
print('arithmetic progression from 0 to 9 = range(10)')
print(range(10))
print('arithmetic progression from 5 to 9 = range(5, 10)')
print(range(5, 10))
print('arithmetic progression from 0 to 9 in steps of 3 = range(0, 10, 3)')
print(range(0, 10, 3))
print('arithmetic degression from -10 to -100 in steps of -30 = range(-10, -100, -30)')
print(range(-10, -100, -30))

# calculate range to iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print i, a[i]
