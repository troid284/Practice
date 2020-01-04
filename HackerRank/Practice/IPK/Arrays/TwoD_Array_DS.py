#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxHrglasSum = 0 
    zeroFound = False
    
    if len(arr) > 3 and len(arr[0]) > 3:
        for row in range(len(arr)-2) :
            for col in range(len(arr[row])-2) :
                total = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
                
                if total == 0 and  maxHrglasSum <= 0 :
                    zeroFound = True
                    
                if zeroFound :
                    maxHrglasSum = max(maxHrglasSum , total)
                else :
                    if maxHrglasSum == 0 and total <= 0 :
                        maxHrglasSum = total                     
                    else :
                        maxHrglasSum = max(maxHrglasSum , total)
    return maxHrglasSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
