#!/usr/bin/env python

def funktion(a, b, *weitere):
    print "Feste Parameter:", a, b
    print "Weitere Parameter:", weitere

funktion(1, 2)
funktion(1, 2, "Hallo Welt", 42, [1,2,3,4])
