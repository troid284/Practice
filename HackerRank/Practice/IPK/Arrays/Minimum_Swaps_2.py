#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    indexArr = [0] * len(arr)
    i,j,minSwaps,x,y = 0,0,0,0,0
    firstIndex, secIndex = 0,0
    print(arr,"\n")
    while i < len(arr) :
        indexArr[arr[i]-1] = i
        i += 1
    print(indexArr,"\n")
        
    while j < len(arr) :
        if arr[j] != (j+1) :
            firstIndex = indexArr[j]
            secIndex = indexArr[arr[j]-1]            
            x = arr[firstIndex]
            y = arr[secIndex]
            arr[secIndex] = x
            indexArr[x-1] = secIndex
            arr[firstIndex] = y
            indexArr[y-1] = firstIndex
            minSwaps += 1  
        j += 1
        
    return minSwaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
