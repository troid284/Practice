#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    i = 0
    while i < len(note) :
        try :
            if magazine.pop(magazine.index(note[i])) != None :
                i += 1
        except ValueError :
            print ("No")
            return            
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
