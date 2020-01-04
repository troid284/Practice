#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0                                   
    jump = 0
    
    while (len(c) > 1) and (i+1 < len(c)) and c[i] == 0:    # Check if current cloud is OK and next cloud is accessible for jump
        if i+2 < len(c) :
            if c[i+2] == 0 :                                # Check if next to next cloud is accessible for jump
                jump += 1
                i += 2        
            elif c[i+1] == 0 :
                jump += 1
                i += 1
            else:
                break
        else :
            if c[i+1] == 0 :                                # Check if immediate next cloud is accessible for jump
                jump += 1
                i += 1
            else:
                break
            
    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
