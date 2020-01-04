#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    manipArr = [0] * n    
    
    i = 0
    while i < len(queries) : 

        manipArr[(queries[i][0])-1] = manipArr[(queries[i][0])-1] + queries[i][2]
           
        if queries[i][1] < n :
            manipArr[queries[i][1]] = manipArr[queries[i][1]] - queries[i][2]

        i += 1
    
    
    maxSum, tempSum, k = 0,0,0
    while k < n :
        if manipArr[k] != 0 :
            tempSum = tempSum + manipArr[k]
            
        maxSum = max(tempSum, maxSum)
        k += 1          
                  
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
