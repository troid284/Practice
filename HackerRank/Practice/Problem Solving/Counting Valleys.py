#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    noOfValleys = 0             # varaible to count no of valleys
    seaLevel    = 0             # value 0 means at sea level
    i=0
    
    primaryCheck = (s.count('D') == s.count('U')) and ((s.count('D') + s.count('U')) == n) and n>=2 and n<=10**6 # This will check primary requirements to run the function
    
    while i<n and primaryCheck:
        if s[i]=='D':
            seaLevel -= 1          # substract 1 for 'D'
            i+=1
        else:
            seaLevel += 1          # add 1 for 'U'
            if seaLevel == 0 :     # String is 'U' and seaLevel is 0 means valley is climbed completely
                noOfValleys += 1   # Increment as valley is climbed 
            i+=1
    return noOfValleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
