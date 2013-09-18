#!/usr/bin/env python

def funktion(a, b, **weitere):
    print "Feste Parameter:", a, b
    print "Weitere Parameter:", weitere

funktion(1, 2)
funktion(1, 2, johannes="ernesti", peter="kaiser")
