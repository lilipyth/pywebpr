#!/usr/bin/env python

a = [66.25, 333, 333, 1, 1234.5]
# return the number of times x appears in the list.
print(a.count(333), a.count(66.25), a.count('x'))

# insert element at given index insert(index, value)
a.insert(2, -1)

# add an item to the end of the list
a.append(333)
print(a)

# return the index in the list of the first item whose value is x. it is an error if there is no such item.
a.index(333)

# remove the first item from the list whose value is x 
a.remove(333)
print(a)

# reverse the list.
a.reverse()
print(a)

a.sort()
print(a)
