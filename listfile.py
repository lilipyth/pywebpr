#!/usr/bin/env python

import os
os.chdir("/Users/mleitner/Repositories/private/python/webProginPython")

def listfile(name): 
    f=open(name)
    L=f.readline()
    while L :
            print L,
            L=f.readline()
    f.close()
