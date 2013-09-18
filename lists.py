#!/usr/bin/env python 

# Lists in python are like arrays in other languages.
# Actually they ale like flex- or dynamic arrays, whose size can change
# during program execution.
# They are not assigned a type. Only the Values inside them have txpes.

a=['spam', 'eggs', 100, 1234]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# a slice operation returns a new list containing the requested elements
print(a[1:-1])
print(a[:2] + ['bacon', 2*2])
print 3*a[:3] + ['Boo!']

# make a shallow copy of the list using slices

b = a[:]
print(b)

# unlike strings, which are immutable, it is possible to change individual elements of a list.
print(a)
a[2] = a[2] + 23
print(a)

# Replace some items: 
a[0:2] = [1, 12]
print(a)

# Remove some items:
a[0:2] = []
print(a)

# Insert some items: 
a[1:1] = ['bletch', 'xyzzy']
print(a)

# Insert (a copy of) itself at the beginning
a[:0] = a
print(a)

# Clear the list: replace all items with an empty list
a[:] = []
print(a)

# the built-in function len() also applies to lists:
b = ['a', 'b', 'c', 'd']
print(len(b))

# it is possible to nest lists (create lists containing other lists), for example:
q = [2, 3]
p = [1, q, 4]
print(len(p))
print(p)
print(p[1])

# print the list q, which is nested in the list p, by accessing the according index of list p
print(p[1])

# print the element at index 0 of list q which is embedded in list p at index 2
print(p[1][0])

# append an element to list q by calling append through the element with index 1 of list p
p[1].append('xtra')
print(len(p))
print(p)
print(p[1])
