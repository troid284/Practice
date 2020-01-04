#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    noOfa = 0                               
    noOfaInRepeatString = s.count('a')
    
    if noOfaInRepeatString > 0 :
        noOfPosRepeats = n // len(s)            # Count number of complete possible string repeats
        noOfLastChar = n % len(s)               # Count number of characters required for last string of complete n characters
        slicedString = s[0 : noOfLastChar]      # Slice the repeat string to calculate number of a's
        noOfa = (noOfPosRepeats * noOfaInRepeatString) + slicedString.count('a')
        
    return noOfa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
