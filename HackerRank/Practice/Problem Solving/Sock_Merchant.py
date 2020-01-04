#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sockcount = 0                           # Initilization of socks count
    ar.sort()                               # Sorting list will arrange socks according to color
    ar.append('end')                        # To end comparison
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            sockcount = sockcount+1
            i+=2                            # If sock color match found then skip the next sock
        else:
            i+=1                            # If sock color is unmatched then check next sock
    return sockcount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
