!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    i, minBribes = 0,0
    chaosArr = [0] * len(q)
    
    while (i < len(q)) :
        
        if i == 0 :
            bribeFound = False
            
        if chaosArr[q[i]-1] < 3 :
            if (i+1) < len(q) :
                if q[i] > q[i+1] :
                    q[i+1], q[i] = q[i], q[i+1]
                    minBribes += 1
                    chaosArr[q[i+1]-1] += 1
                    bribeFound = True
        else:
            print("Too chaotic")
            i = len(q)+1
            return 
        
        if bribeFound and (i >= (len(q)-1)) :
            i = 0
        else:
            i += 1
            
    if i != (len(q)+1):   
        print (minBribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
