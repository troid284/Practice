#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    i,count = 1,0
    while i < len(s) : 
        j = 0
        while (j+i) < len(s):
            k = 1
            while j+k+i < len(s)+1 : 
                if sorted(s[j:j+i]) == sorted(s[j+k:j+k+i]) :
                    count += 1;
                k += 1
            j += 1
        i += 1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
